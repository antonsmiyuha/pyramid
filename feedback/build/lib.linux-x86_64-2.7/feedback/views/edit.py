import logging

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError

from ..models import feedback


@view_config(route_name='edit', renderer='../templates/edit.mako')
def feedback_edit(request):
    feedback_id = int(request.GET['id'])
    try:
        feedback_entity = request.dbsession.query(feedback.Feedback).filter_by(id=feedback_id).one()
        if feedback_entity.status == 'new':
            feedback_entity.status = 'read'
            request.dbsession.add(feedback_entity)
            request.dbsession.flush()
    except DBAPIError as e:
        logging.exception(e.message)
        request.session.flash('Some Error Occurred')
        return HTTPFound(location='/list')

    return {'data': feedback_entity}
