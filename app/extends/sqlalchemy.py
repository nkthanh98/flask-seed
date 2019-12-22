#coding=utf-8

import enum
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import (
    Migrate,
    MigrateCommand,
)
from sqlalchemy import (
    Column,
    Integer,
    TIMESTAMP,
    func,
)


db = SQLAlchemy()
migrate = Migrate(db=db)


class TimestampModel:
    updated_at = Column(TIMESTAMP, onupdate=func.now())
    created_at = Column(TIMESTAMP, default=func.now())


class IdentityModel:
    id = Column(Integer, primary_key=True, autoincrement=True)


class EnumBase(enum.Enum):
    @classmethod
    def values(cls):
        return list(map(lambda c: c.value, cls))
