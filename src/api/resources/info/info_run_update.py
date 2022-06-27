import json
import requests
from rest_core import Resource
from marshmallow import fields
from marshmallow_core import (
    ApiSchema,
)
from models import (
    HostInfo,
)
from extensions.postgresql import db


class InfoRunUpdate(Resource):

    def post(self):
        # запустить ansible-playbook, который будет опрашивать сервисы Ambari

        # stats = callbacks.AggregateStats()
        # playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
        # inventory = ansible.inventory.Inventory(ANSIBLE_HOSTS)
        # runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)
        #
        # pb = ansible.playbook.PlayBook(playbook=PLAYBOOK,
        #                                callbacks=playbook_cb,
        #                                runner_callbacks=runner_cb,
        #                                stats=stats,
        #                                inventory=inventory,
        #                                extra_vars={'name': "AAA"})
        # pb.run()

        hosts = {
            'c1': ['host1', 'host2'],
            'c2': ['host1', 'host2']
        }

        for cluster, hosts in hosts.items():
            for host in hosts:
                r = requests.get(f'http://127.0.0.1:5222/api/v1/clusters/{cluster}/hosts/{host}')

                data = {'info': json.dumps(r.json())}

                new_info = HostInfo(cluster=cluster, host=host, info=data['info'])

                db.session.add(new_info)
                db.session.commit()

        # r = requests.get('http://127.0.0.1:5222/api/v1/clusters/c1/hosts/host1')
        #
        # data = {'info': json.dumps(r.json())}
        #
        # new_info = HostInfo(info=data['info'])
        #
        # db.session.add(new_info)
        # db.session.commit()

        res = {'message': 'new info added to db'}
        return ResponseSchema().dump(res)


class ResponseSchema(ApiSchema):

    # id = fields.Str(default=None)
    message = fields.Str(default=None)
