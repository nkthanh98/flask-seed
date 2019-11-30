# coding=utf-8

from flask import Flask
from .examples import example_ns


def register_namespace(app: Flask):
    app.register_blueprint(example_ns, url_prefix='')
