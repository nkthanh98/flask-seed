# coding=utf-8

import logging
from werkzeug import exceptions as exc
from flask import g
from app.extends.flask import (
    Namespace,
    MethodView
)
from app import schemas
from app.services import PetService


pet_ns = Namespace('pet', __name__)


@pet_ns.route('/pet', methods=['POST'])
class PetCreator(MethodView):
    @pet_ns.expect(schemas.Pet)
    @pet_ns.marshal_with(schemas.Pet)
    def post(self):
        service = PetService()
        return service.create_pet(g.json)


@pet_ns.route('/pet/<int:pet_id>', methods=['GET', 'PATCH', 'DELETE'])
class Pet(MethodView):
    @pet_ns.marshal_with(schemas.Pet)
    def get(self, pet_id):
        service = PetService()
        pet = service.get_pet(pet_id)
        if pet:
            return pet
        raise exc.NotFound('Pet not found')

    @pet_ns.expect(schemas.Pet)
    @pet_ns.marshal_with(schemas.Pet)
    def patch(self, pet_id):
        service = PetService()
        return service.update_pet(pet_id, g.json)

    @pet_ns.marshal_with(schemas.Pet)
    def delete(self, pet_id):
        service = PetService()
        return service.delete_pet(pet_id)

