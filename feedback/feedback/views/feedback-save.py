from pyramid.response import Response
from pyramid.request import Request
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import feedback
from ..error.validation import ValidationException
import requests
import datetime
import json


@view_config(route_name='feedback-save')
def my_view(request):
    try:
        post = request.POST
        request.session['feedback_data'] = post

        name = post['name']
        email = post['email']
        phone = post['phone']
        subject = post['subject']
        message = post['message']

        if not name:
            raise ValidationException('Invalid Name', 0)

        if not email:
            raise ValidationException('Invalid Email', 1)

        if not phone:
            raise ValidationException('Invalid Phone', 2)

        if not subject:
            raise ValidationException('Invalid Subject', 3)

        if not message:
            raise ValidationException('Invalid Message', 4)

        url = 'https://www.google.com/recaptcha/api/siteverify'

        data = {
            'secret': '6LdiIhoUAAAAAIUI3VxTvhr2zRnWDYeKTFrtpkZV',
            'response': post['g-recaptcha-response']
        }

        response = requests.post(url=url, data=data)
        decoded_response = json.loads(response.text)

        if decoded_response['success'] != 'True':
            raise ValidationException('Invalid Captcha', 5)

        feedback_entity = feedback.Feedback()
        feedback_entity.name = name
        feedback_entity.email = email
        feedback_entity.phone = phone
        feedback_entity.subject = subject
        feedback_entity.message = message
        feedback_entity.created_at = datetime.datetime.now()
        feedback_entity.updated_at = datetime.datetime.now()
        feedback_entity.customer_ip = request.remote_addr

        request.dbsession.add(feedback_entity)
        return HTTPFound(location='/feedback')

    except ValidationException, e:
        request.session.flash(e.get_message())
        return HTTPFound(location='/feedback')

    except Exception, e:
        return {'exception': e}
