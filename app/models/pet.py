#coding=utf-8

from sqlalchemy import (
    String,
    Enum,
    Column,
)
from app.extends import (
    db,
    TimestampModel,
    IdentityModel,
    EnumBase,
)


class PetStatus(EnumBase):
    avaiable = 'avaiable'
    pending = 'pending'
    sold = 'sold'


class Pet(db.Model, IdentityModel, TimestampModel):
    name = Column(String(40), nullable=False)
    status = Column(Enum(PetStatus), nullable=False)
    owner_name = Column(String(50), nullable=False)
