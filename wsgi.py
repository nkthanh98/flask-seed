# coding=utf-8

import os

from app import create_app

ENV = os.getenv('FLASK_ENV', 'development')

wsgi_app = create_app(ENV)
