#coding=utf-8

from unittest import TestCase
from flask.testing import Client
import pytest
from faker import Faker


fake = Faker()

@pytest.mark.usefixtures('test_client')
class BaseTestCase(TestCase):
    support_methods = ('GET', 'PUT', 'PATCH', 'POST', 'DELETE',)

    client: Client = None   # Flask test client

    path: str = None

    method: str = None

    content_type: str = 'application/json'

    def call_api(self, path=None, method=None, data=None, json=None,
                 content_type=None, headers=None):
        path = path or self.path
        method = method or self.method
        content_type = content_type or self.content_type

        assert path is not None, 'Method must be string'
        assert method in self.support_methods, \
            f'Method must be one of {self.support_methods}'

        if method.upper() == 'GET':
            return self.client.open(
                path=path,
                method='GET',
                headers=headers
            )
        if content_type == 'application/json':
            return self.client.open(
                path=path,
                method=method,
                json=json,
                headers=headers,
                content_type='application/json'
            )
        return self.client.open(
            path=path,
            method=method,
            data=data,
            headers=headers,
            content_type=content_type
        )
