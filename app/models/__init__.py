# coding=utf-8

from app.extends import (
    db,
    migrate,
)
from .pet import Pet


def init_app(app):
    db.init_app(app)
    migrate.init_app(app)
