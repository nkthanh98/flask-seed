# coding=utf-8

from flask import Flask
from werkzeug.contrib.profiler import ProfilerMiddleware

from . import config
from . import logging
from . import helpers
from . import extends
from . import exceptions
from . import schemas
from . import models
from . import repository
from . import validators
from . import services
from . import routes


def create_app(config_name):
    """create_app

    :param config_name:
    """
    app = Flask(__name__)
    app.config.from_object(config.get_config(config_name))
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, stream=None,
                                      profile_dir=app.config['CPROF_DIR'])

    logging.init_app(app)
    exceptions.init_app(app)
    routes.init_app(app)

    return app
