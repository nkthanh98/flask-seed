# coding=utf-8

import logging
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug import exceptions as exc
from flask import (
    Blueprint,
    request,
    g,
    jsonify,
    views,
    Response
)


logger = logging.getLogger('request')


class MethodView(views.MethodView):
    def dispatch_request(self, *args, **kwargs):
        logger.info(f'{request.environ["REMOTE_ADDR"]} - {request.environ["REQUEST_URI"]} - {request.environ["REQUEST_METHOD"]}')
        setattr(g, 'json', request.json)
        setattr(g, 'args', request.args)
        return super().dispatch_request(*args, **kwargs)


class Namespace(Blueprint):
    def route(self, rule, **options):
        def decorator(handler):
            endpoint = options.pop('endpoint', handler.__name__)
            f = handler
            if isinstance(handler, type) and issubclass(handler, MethodView):
                f = handler.as_view(endpoint)
            self.add_url_rule(rule, endpoint, f, **options)
            return handler
        return decorator

    def expect(self, schema_cls):
        def outer_fn(func):
            def decorator(*args, **kwargs):
                schema = schema_cls()
                errors = schema.validate(g.json)
                if errors:
                    validate_exc = exc.BadRequest()
                    setattr(validate_exc, 'errors', errors)
                    raise validate_exc
                else:
                    data = schema.load(g.json)
                    setattr(g, 'json', ImmutableMultiDict(data.items()))
                return func(*args, **kwargs)
            return decorator
        return outer_fn

    def marshal_with(self, schema_cls):
        def outer_fn(func):
            def decorator(*args, **kwargs):
                ret = func(*args, **kwargs)
                schema = schema_cls()
                marshal_result = schema.dump(ret)
                if marshal_result.errors:
                    raise exc.InternalServerError()
                return jsonify(**marshal_result.data)
            return decorator
        return outer_fn
