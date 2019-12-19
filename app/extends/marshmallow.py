# coding=utf-8

import re

from marshmallow import (
    Schema as BaseSchema,
    pre_load,
    post_load
)


def _snake_case_to_camel_case(name):
    def _camel(match):
        return match.group(1) + match.group(2).upper()

    return re.sub(r"(.*?)_([a-zA-Z])", _camel, name, 0)


class Schema(BaseSchema):
    def on_bind_field(self, name, obj):
        obj.data_key = _snake_case_to_camel_case(obj.data_key or name)

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

    @post_load
    def remove_extra_field(self, data, **kwargs):
        """remove_extra_field

        :param data:
        """
        if data is not None:
            ret = {}
            for key, _ in self.fields.items():
                if key in data:
                    ret[key] = data[key]
            return ret
        return None
