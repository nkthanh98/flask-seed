# coding=utf-8

import logging
from app.extends import (
    db,
    migrate,
)
from .pet import Pet


def init_app(app):
    db.init_app(app)
    migrate.init_app(app)

    logging.getLogger('model').info(
        f'App connected to `{app.config["DB_NAME"]}` database'
    )
