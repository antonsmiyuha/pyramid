def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('feedback', '/feedback')
    config.add_route('feedback-save', '/feedback/save')
    config.add_route('list', '/list')
