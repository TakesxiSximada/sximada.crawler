# -*- coding: utf-8 -*-

from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def serve(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('sximada.app.timeline.debug', '/debug')
    config.add_route('sximada.app.timeline.ping', '/ping')
    config.add_static_view('', 'static', cache_max_age=3600)
    config.scan()
    return config.make_wsgi_app()
