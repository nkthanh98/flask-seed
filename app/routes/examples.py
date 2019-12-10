# coding=utf-8

from werkzeug.exceptions import BadGateway

from app.extends.flask import (
    Namespace,
    MethodView
)
from app import schemas


example_ns = Namespace('examples', __name__)


@example_ns.route('/examples')
class ExampleResource(MethodView):
    @example_ns.expect(schemas.ExamplePost)
    def post(self):
        return {'name': 'Thanh', 'age': 20}
