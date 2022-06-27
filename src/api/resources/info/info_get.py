from rest_core import Resource
from marshmallow import fields
from marshmallow import EXCLUDE
from marshmallow.validate import Range
from marshmallow_core import (
    ApiSchema,
)
from models import (
    HostInfo,
)
# from extensions.postgresql import db
from .schemas import InfoSchema


# class InfoSchema(ApiSchema):
#
#     info = fields.Str(default=None)
#     created_date = fields.DateTime(default=None)
#     cluster = fields.Str(default=None)
#     host = fields.Str(default=None)


class FiltersSchema(ApiSchema):

    start = fields.Int(default=None, missing=0, validate=Range(min=0))
    limit = fields.Int(default=None, missing=50, validate=Range(min=0))


class SerializationSchema(ApiSchema):

    items = fields.Nested(InfoSchema, many=True)
    totals = fields.Int()
    filters = fields.Nested(FiltersSchema)


class InfoGet(Resource):

    def get(self, info_id):
        filters = FiltersSchema().deserialize(self.request.args, unknown=EXCLUDE)

        info = HostInfo.query.get(info_id)

        print(info)

        # items = [
        #     {
        #         'cluster': info.cluster,
        #         'host': info.host,
        #         'info': info.info,
        #         'created_date': info.created_date
        #     }
        #     for info in infos
        # ]

        return InfoSchema().serialize(info)
