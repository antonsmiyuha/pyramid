from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
import logging


@view_config(route_name='feedback', renderer='../templates/feedback.mako')
def my_view(request):
    validate_error = request.session.pop_flash()
    try:
        if request.session['feedback_data']:
            feedback_data = request.session['feedback_data']
            request.session['feedback_data'] = None
        else:
            feedback_data = []
    except KeyError:
        feedback_data = []

    logging.error('test')

    return {'errors': validate_error, 'data': feedback_data}
