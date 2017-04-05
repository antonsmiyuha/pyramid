from pyramid.view import view_config


@view_config(route_name='feedback', renderer='../templates/feedback.mako')
def feedback(request):
    try:
        session_data = request.session['feedback_data']
        request.session['feedback_data'] = None
    except KeyError:
        session_data = None

    return {'data': session_data}
