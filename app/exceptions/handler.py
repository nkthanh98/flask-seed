# coding=utf-8

import logging
import json
from werkzeug.exceptions import InternalServerError


logger = logging.getLogger('route')


def http_exc_handler(exc):
    resp = exc.get_response()
    resp.data = json.dumps({
        'message': exc.description,
        'name': exc.name,
        'errors': getattr(exc, 'errors', None)
    })
    resp.content_type = 'application/json'
    return resp


def generic_exc_handler(exc):
    logger.exception('')

    resp = InternalServerError().get_response()
    resp.data = json.dumps({
        'message': 'Server error',
    })
    resp.content_type = 'application/json'
    return resp
