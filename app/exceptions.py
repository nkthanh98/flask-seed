# coding=utf-8
"""
Define exception handler
"""

import logging
import json
from werkzeug.exceptions import (
    HTTPException,
    InternalServerError
)


logger = logging.getLogger('werkzeug') # pylint:disable=C0103


def http_exc_handler(exc):
    """http_exc_handler

    :param exc:
    """
    resp = exc.get_response()
    resp.data = json.dumps({
        'message': exc.description,
        'name': exc.name,
        'errors': getattr(exc, 'errors', None)
    })
    resp.content_type = 'application/json'
    return resp


def generic_exc_handler(exc): # pylint:disable=W0613
    """generic_exc_handler

    :param exc:
    """
    logger.exception('')

    resp = InternalServerError().get_response()
    resp.data = json.dumps({
        'message': 'Server error',
    })
    resp.content_type = 'application/json'
    return resp


def init_app(app):
    """init_app

    :param app:
    """
    app.register_error_handler(Exception, generic_exc_handler)
    app.register_error_handler(HTTPException, http_exc_handler)
