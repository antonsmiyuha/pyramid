from __future__ import division
import math
import logging

from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from pyramid.httpexceptions import HTTPFound

from ..models import feedback


@view_config(route_name='list', renderer='../templates/list.mako')
def my_view(request):
    per_page = 9

    try:
        page = int(request.GET['page'])
        if not page:
            page = 1
    except KeyError:
        page = 1

    offset = (page - 1) * per_page
    try:
        collection = request.dbsession.query(feedback.Feedback).order_by(feedback.Feedback.id.desc()).limit(
            per_page).offset(offset)
        pages = int(math.ceil(request.dbsession.query(feedback.Feedback.id).count() / per_page)) + 1
    except DBAPIError as e:
        logging.exception(e.message)
        request.session.flash('Some Error Occurred')
        return HTTPFound(location='/feedback')

    return {'collection': collection, 'pages': pages}
