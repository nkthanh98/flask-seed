# coding=utf-8

from werkzeug.exceptions import HTTPException

from .handler import (
    http_exc_handler,
    generic_exc_handler
)


def init_app(app):
    """init_app

    :param app:
    """
    app.register_error_handler(Exception, generic_exc_handler)
    app.register_error_handler(HTTPException, http_exc_handler)
