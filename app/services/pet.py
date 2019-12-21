#coding=utf-8

from app.models import Pet as PetModel
from app.models.pet import PetStatus
from app.repository.pet import PetRepository


class Pet:
    def get_pet(self, pet_id):
        repository = PetRepository()
        return repository.get_pet(pet_id)

    def create_pet(self, data):
        pet = PetModel(
            name=data.get('name', 'Bob'),
            status=data.get('status', PetStatus.avaiable),
            owner_name=data.get('owner_name', 'David')
        )
        return pet

    def update_pet(self, pet_id, data):
        repository = PetRepository()
        pet = repository.get_pet(pet_id)
        if 'name' in data:
            pet.name = data['name']
        if 'status' in data:
            pet.status = data['status']
        if 'owner_name' in data:
            pet.owner_name = data['owner_name']
        return pet

    def delete_pet(self, pet_id):
        repository = PetRepository()
        pet = repository.get_pet(pet_id)
        return pet
