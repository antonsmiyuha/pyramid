import logging

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError

from ..models import feedback


@view_config(route_name='delete')
def delete_feedback(request):
    if not int(request.GET['id']):
        logging.error('invalid id')
        request.session.flash('Some Error Occurred')
        return HTTPFound(location='/list')

    try:
        feedback_entity = request.dbsession.query(feedback.Feedback).filter_by(id=request.GET['id']).one()
        request.dbsession.delete(feedback_entity)
        request.dbsession.flush()
    except DBAPIError as e:
        logging.error(e.message)
        request.session.flash('Some Error Occurred')
        return HTTPFound(location=request.route_url('edit', _query={'id': request.GET['id']}))

    return HTTPFound(location='/list')
