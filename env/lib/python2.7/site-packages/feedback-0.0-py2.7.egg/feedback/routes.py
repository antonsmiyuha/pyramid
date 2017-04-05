def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('feedback', '/feedback')
    config.add_route('save', '/feedback/save')
    config.add_route('list', '/list')
    config.add_route('edit', '/edit')
    config.add_route('update', '/update')
    config.add_route('delete', '/delete')
