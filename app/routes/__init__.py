# coding=utf-8

from .examples import example_ns


def init_app(app):
    app.register_blueprint(example_ns, url_prefix='')
