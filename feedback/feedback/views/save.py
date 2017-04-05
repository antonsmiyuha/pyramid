import re
import logging
import datetime
import json

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
import requests

from ..models import feedback


@view_config(route_name='save')
def save_feedback(request):
    post = request.POST
    request.session['feedback_data'] = post

    try:
        if not post.getone('name'):
            request.session.flash('Invalid Name')
            return HTTPFound(location='/feedback')

        if not post.getone('email') or not re.match(r"^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$",
                                                    post.getone('email')):
            request.session.flash('Invalid Email')
            return HTTPFound(location='/feedback')

        if not post.getone('phone'):
            request.session.flash('Invalid Phone')
            return HTTPFound(location='/feedback')

        if not post.getone('subject'):
            request.session.flash('Invalid Subject')
            return HTTPFound(location='/feedback')

        if not post.getone('message'):
            request.session.flash('Invalid Message')
            return HTTPFound(location='/feedback')

        if not post.getone('g-recaptcha-response'):
            request.session.flash('Invalid Captcha')
            return HTTPFound(location='/feedback')
    except KeyError:
        request.session.flash('Some Error Occurred')
        return HTTPFound(location='/feedback')

    url = 'https://www.google.com/recaptcha/api/siteverify'

    data = {
        'secret': '6LdiIhoUAAAAAIUI3VxTvhr2zRnWDYeKTFrtpkZV',
        'response': post['g-recaptcha-response']
    }

    response = requests.post(url=url, data=data)
    decoded_response = json.loads(response.text)

    # if decoded_response['success'] != 'True':
    #     request.session.flash('Invalid Captcha')
    #     return HTTPFound(location='/feedback')

    feedback_entity = feedback.Feedback()
    feedback_entity.name = post.getone('name')
    feedback_entity.email = post.getone('email')
    feedback_entity.phone = post.getone('phone')
    feedback_entity.subject = post.getone('subject')
    feedback_entity.message = post.getone('message')
    feedback_entity.created_at = datetime.datetime.now()
    feedback_entity.updated_at = datetime.datetime.now()
    feedback_entity.status = 'new'
    feedback_entity.customer_ip = request.remote_addr

    try:
        request.dbsession.add(feedback_entity)
        request.dbsession.flush()
        request.session.flash('Thank you for your feedback')
        return HTTPFound(location='/list')
    except DBAPIError as e:
        logging.exception(e.message)
        request.session.flash('Some Error Occurred')
        return HTTPFound(location='/feedback')
