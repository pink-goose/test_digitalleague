from marshmallow import fields
from marshmallow_core import (
    ApiSchema,
)


class InfoSchema(ApiSchema):

    info = fields.Str(default=None)
    created_date = fields.DateTime(default=None)
    cluster = fields.Str(default=None)
    host = fields.Str(default=None)
