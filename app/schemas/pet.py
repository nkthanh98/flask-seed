# coding=utf-8

from marshmallow import (
    fields,
    validate,
)
from app.models.pet import PetStatus
from app.extends import Schema



class PetStatusValidator(validate.Validator):
    def __call__(self, value):
        if value not in PetStatus.values():
            raise validate.ValidationError(
                f'status must be one of {PetStatus.values}'
            )
        return value


class Pet(Schema):
    name = fields.String(required=True)
    status = fields.String(attribute='status.value')
    owner_name = fields.String(required=True)
