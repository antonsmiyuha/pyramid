from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import feedback


@view_config(route_name='list', renderer='../templates/list.mako')
def my_view(request):
    try:
        page = 1
        feedback_entity = feedback.Feedback
        collection = request.dbsession.query(feedback_entity).limit(page * 20)
        pages = 100 // 20
        return {'collection': collection, 'pages': pages}
    except Exception as e:
        print('test')
        print(e.message)
        return {'exception': e}
