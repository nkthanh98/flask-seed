#coding=utf-8

from app.models import Pet
from tests.extends import (
    fake,
    BaseFactory,
)

class PetFactory(BaseFactory):
    class Meta:
        model = Pet

    name = fake.name()
    owner_name = fake.name()
    status = 'avaiable'
