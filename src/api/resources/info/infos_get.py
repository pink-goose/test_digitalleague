import json
from rest_core import Resource
from marshmallow import (
    EXCLUDE,
    # pre_load,
    fields
)
from marshmallow.validate import Range
from marshmallow_core import (
    ApiSchema
)
from models import (
    HostInfo,
)
# from extensions.postgresql import db
from .schemas import InfoSchema


class FiltersSchema(ApiSchema):

    start = fields.Int(default=None, missing=0, validate=Range(min=0))
    limit = fields.Int(default=None, missing=50, validate=Range(min=0))
    # clusters = fields.List(fields.Str, default=None)
    # hosts = fields.List(fields.Str, default=None)
    #
    # @pre_load(pass_many=True)
    # def pre_load_handler(self, data, **kwargs):
    #     data = data.to_dict()
    #     if 'clusters' in data:
    #         data['clusters'] = data['clusters'].split(',')
    #     if 'hosts' in data:
    #         data['hosts'] = data['hosts'].split(',')
    #     print(data)
    #     return data


class SerializationSchema(ApiSchema):

    items = fields.Nested(InfoSchema, many=True)
    totals = fields.Int()
    filters = fields.Nested(FiltersSchema)


class InfosGet(Resource):

    def get(self):

        filters = FiltersSchema().deserialize(self.request.args, unknown=EXCLUDE)

        # infos = HostInfo.query.filter(HostInfo.cluster.in_(filters['clusters'])).limit(filters['limit']).offset(
        # filters['start']).all()

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
