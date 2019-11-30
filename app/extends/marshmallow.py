# coding=utf-8

from marshmallow import (
    Schema as BaseSchema,
    pre_load
)


class Schema(BaseSchema):
    class Meta:
        strict = False

    @pre_load
    def strip(self, data, **kwargs):
        """strip text data from request.json
        data: Union[str, list, int, float, dict]

        :param data:
        """
        if isinstance(data, str):
            return data.strip()
        if isinstance(data, list):
            return [self.strip(val) for val in data]
        if isinstance(data, dict):
            return {key: self.strip(val) for key, val in data.items()}
        return data

    @pre_load
    def remove_extra_field(self, data, **kwargs):
        """remove_extra_field

        :param data:
        """
        ret = {}
        for key, _ in self.fields.items():
            ret[key] = data.get(key)
        return ret
