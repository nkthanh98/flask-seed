#coding=utf-8

from unittest.mock import patch
from tests.extends import (
    BaseTestCase,
    fake,
)
from tests.factories import PetFactory


class PetAPITestCase(BaseTestCase):
    def setUp(self):
        self.pet = PetFactory()

    @patch('app.services.PetService.get_pet')
    def test_get_pet(self, mock):
        mock.return_value = self.pet
        resp = self.call_api(
            path=f'/pet/{self.pet.id}',
            method='GET',
        )
        assert resp.status_code == 200
        assert resp.json['name'] == self.pet.name
        assert resp.json['status'] == self.pet.status.value
        assert resp.json['ownerName'] == self.pet.owner_name
