from marshmallow import (
    Schema,
    ValidationError,
)
from rest_core.exceptions import DataError


class ApiSchema(Schema):

    def deserialize(self, data, many=None, unknown=None):
        try:
            data = self.load(data, many=many, unknown=unknown)
        except ValidationError as e:
            raise DataError(e.messages)
        return data

    def serialize(self, data, many=None):
        return self.dump(data, many=many)
