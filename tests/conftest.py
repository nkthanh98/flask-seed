#coding=utf-8

import pytest
from app import create_app
from app.models import db


@pytest.fixture(scope='class')
def test_client(request):
    if request.cls is not None:
        flask_app = create_app('testing')
        client = flask_app.test_client()
        ctx = flask_app.app_context()
        ctx.push()
        db.create_all()
        request.cls.client = client
        yield

        ctx.pop()
