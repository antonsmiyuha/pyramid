from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.set_session_factory(SignedCookieSessionFactory('itsaseekreet'))
    config.include('pyramid_jinja2')
    config.include('pyramid_mako')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
