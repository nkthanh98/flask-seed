# coding=utf-8

from .pet import pet_ns


def init_app(app):
    app.register_blueprint(pet_ns, url_prefix='')
