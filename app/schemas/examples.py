# coding=utf-8

from marshmallow import fields

from app.extends import Schema


class ExamplePost(Schema):
    full_name = fields.String(required=True)
    age = fields.Integer()
