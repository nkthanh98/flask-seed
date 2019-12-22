#coding=utf-8

from werkzeug import exceptions as exc
from app.models import Pet as PetModel
from app.models import db
from app.models.pet import PetStatus


class PetRepository:
    def get_pet(self, pet_id):
        return PetModel.query.filter(
            PetModel.id == pet_id
        ).first()

    def create_pet(self, name, status, owner_name):
        pet = PetModel(
            name=name,
            status=status,
            owner_name=owner_name
        )
        db.session.add(pet)
        db.session.commit()
        return pet

    def update_pet(self, pet_id, data):
        pet = self.get_pet(pet_id)
        if pet is None:
            raise exc.NotFound('Pet not found')
        if 'name' in data:
            pet.name = data['name']
        if 'status' in data:
            pet.status = data['status']
        if 'owner_name' in data:
            pet.owner_name = data['owner_name']
        db.session.add(pet)
        db.session.commit()
        return pet

    def delete_pet(self, pet_id):
        pet = self.get_pet(pet_id)
        if pet is None:
            raise exc.NotFound('Pet not found')
        db.session.delete(pet)
        db.session.commit()
        return pet
