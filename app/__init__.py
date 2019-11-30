# coding=utf-8

import os
import logging.config
from flask import Flask

from . import config
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

    logging.config.fileConfig(
        fname=os.path.join(app.config['ROOT_DIR'], 'app', 'config', 'log.ini'),
        defaults={'logfile': app.config['LOG_FILE']},
    )

    routes.register_namespace(app)
    exceptions.init_app(app)

    return app
