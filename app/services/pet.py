#coding=utf-8

from app.models.pet import PetStatus
from app.repository.pet import PetRepository


class PetService:
    repository = PetRepository()

    def get_pet(self, pet_id):
        return self.repository.get_pet(pet_id)

    def create_pet(self, data):
        status = PetStatus.avaiable.value
        if 'status' in data:
            status = data['status']['value']
        pet = self.repository.create_pet(
            name=data.get('name', 'Bob'),
            status=status,
            owner_name=data.get('owner_name', 'David')
        )
        return pet

    def update_pet(self, pet_id, data):
        return self.repository.update_pet(pet_id, data)

    def delete_pet(self, pet_id):
        return self.repository.delete_pet(pet_id)
