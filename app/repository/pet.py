#coding=utf-8

from app.models import Pet as PetModel
from app.models.pet import PetStatus


class PetRepository:
    def get_pet(self, pet_id):
        return PetModel(
            name='Bob',
            status=PetStatus.avaiable,
            owner_name='David'
        )
