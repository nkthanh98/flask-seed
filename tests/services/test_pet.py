#coding=utf-8

from unittest.mock import patch
from tests.extends import (
    BaseTestCase,
    fake,
)
from tests.factories import PetFactory
from app.services import PetService


class PetServiceTestCase(BaseTestCase):
    def setUp(self):
        self.pet = PetFactory(
            name=fake.name(),
            status=fake.random_element(('avaiable', 'sold')),
            owner_name=fake.name()
        )
        self.target = PetService()

    @patch('app.repository.pet.PetRepository.get_pet')
    def test_get_pet(self, mock):
        mock.return_value = self.pet
        ret = self.target.get_pet(self.pet.id)
        assert ret == self.pet
