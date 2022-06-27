from rest_core import Resource
from marshmallow import fields
from marshmallow_core import (
    ApiSchema,
)


class Ping(Resource):

    def get(self):
        res = {'text': 'PONG'}
        return ResponseSchema().dump(res)


class ResponseSchema(ApiSchema):

    text = fields.Str(default=None)
