#coding=utf-8

import pytest
from tests.extends import (
    BaseTestCase,
    fake,
)
from tests.factories import PetFactory
from app.repository.pet import PetRepository
from app.models import Pet as PetModel
from app import exceptions as exc


class PetRepositoryTestCase(BaseTestCase):
    def setUp(self):
        self.pet = PetFactory()
        self.target = PetRepository()

    def test_get_pet(self):
        result = self.target.get_pet(self.pet.id)
        assert self.pet == result

    def test_get_pet_not_found(self):
        result = self.target.get_pet(fake.random_int(2))
        assert result is None

    def test_create_new_pet(self):
        new_pet = self.target.create_pet(
            name=fake.name(),
            status=fake.random_element(('avaiable', 'sold')),
            owner_name=fake.name()
        )
        ret = PetModel.query.filter(
            PetModel.id == new_pet.id
        ).first()
        assert ret == new_pet

    def test_update_pet(self):
        updated_pet = self.target.update_pet(
            pet_id=self.pet.id,
            data={
                'name': fake.text(),
                'status': fake.random_element(('avaiable', 'sold')),
                'owner_name': fake.text()
            }
        )
        assert self.pet == updated_pet

    def test_update_pet_fail(self):
        with pytest.raises(exc.HTTPException):
            self.target.update_pet(
                pet_id=fake.random_int(2),
                data={
                    'name': fake.text(),
                    'status': fake.random_element(('avaiable', 'sold')),
                    'owner_name': fake.text()
                }
            )

    def test_delete_pet(self):
        deleted_pet = self.target.delete_pet(self.pet.id)
        assert self.pet == deleted_pet
        ret = PetModel.query.filter(
            PetModel.id == self.pet.id
        ).first()
        assert ret is None

    def test_delete_pet_fail(self):
        with pytest.raises(exc.HTTPException):
            self.target.delete_pet(pet_id=fake.random_int(2))
