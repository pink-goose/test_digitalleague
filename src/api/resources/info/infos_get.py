import json
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


class FiltersSchema(ApiSchema):

    start = fields.Int(default=None, missing=0, validate=Range(min=0))
    limit = fields.Int(default=None, missing=50, validate=Range(min=0))


class SerializationSchema(ApiSchema):

    items = fields.Nested(InfoSchema, many=True)
    totals = fields.Int()
    filters = fields.Nested(FiltersSchema)


class InfosGet(Resource):

    def get(self):
        filters = FiltersSchema().deserialize(self.request.args, unknown=EXCLUDE)

        infos = HostInfo.query.limit(filters['limit']).offset(filters['start']).all()

        items = [
            {
                'cluster': info.cluster,
                'host': info.host,
                'info': json.loads(info.info),
                'created_date': info.created_date
            }
            for info in infos
        ]

        return SerializationSchema().serialize({'items': items, 'totals': len(items), 'filters': filters})
