import re
import logging
import datetime

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError

from ..models import feedback


@view_config(route_name='update')
def my_view(request):
    post = request.POST

    try:
        if not int(post.getone('id')):
            request.session.flash('Invalid Name')
            return HTTPFound(location='/feedback')

        if not post.getone('name'):
            request.session.flash('Invalid Name')
            return HTTPFound(location=request.route_url('edit', _query={'id': post.getone('id')}))

        if not post.getone('email') or not re.match(r"^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$",
                                                    post.getone('email')):
            request.session.flash('Invalid Email')
            return HTTPFound(location=request.route_url('edit', _query={'id': post.getone('id')}))

        if not post.getone('phone'):
            request.session.flash('Invalid Phone')
            return HTTPFound(location=request.route_url('edit', _query={'id': post.getone('id')}))

        if not post.getone('subject'):
            request.session.flash('Invalid Subject')
            return HTTPFound(location=request.route_url('edit', _query={'id': post.getone('id')}))

        if not post.getone('message'):
            request.session.flash('Invalid Message')
            return HTTPFound(location=request.route_url('edit', _query={'id': post.getone('id')}))

        if not post.getone('status'):
            request.session.flash('Invalid Status')
            return HTTPFound(location=request.route_url('edit', _query={'id': post.getone('id')}))

    except KeyError as e:
        logging.error(e.message)
        request.session.flash('Some Error Occurred')
        return HTTPFound(location='/list')

    feedback_entity = request.dbsession.query(feedback.Feedback).filter_by(id=post.getone('id')).one()
    feedback_entity.name = post.getone('name')
    feedback_entity.email = post.getone('email')
    feedback_entity.phone = post.getone('phone')
    feedback_entity.subject = post.getone('subject')
    feedback_entity.message = post.getone('message')
    feedback_entity.status = post.getone('status')
    feedback_entity.created_at = datetime.datetime.now()
    feedback_entity.updated_at = datetime.datetime.now()
    feedback_entity.customer_ip = request.remote_addr

    try:
        request.dbsession.add(feedback_entity)
        request.dbsession.flush()
        request.session.flash('Updated')
    except DBAPIError as e:
        logging.exception(e.message)
        request.session.flash('Some Error Occurred')

    return HTTPFound(location=request.route_url('edit', _query={'id': post.getone('id')}))
