#coding=utf-8

from factory.alchemy import SQLAlchemyModelFactory
from app.models import db


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = db.session

        sqlalchemy_session_persistence = 'commit'
