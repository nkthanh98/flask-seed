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
    @example_ns.marshal_with(schemas.ExamplePost)
    def post(self):
        class Person:
            def __init__(self):
                self.full_name = 'Thanh'
                self.age = 20
        return Person()
