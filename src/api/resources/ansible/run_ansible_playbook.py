from rest_core import Resource
from marshmallow import fields
from marshmallow_core import (
    ApiSchema,
)
from models import (
    HostInfo,
)
from extensions.postgresql import db
# import ansible.playbook
# from ansible import callbacks
# from ansible import utils
# ANSIBLE_HOSTS = 'hosts'
# PLAYBOOK = 'foo.yml'


class RunAnsiblePlaybook(Resource):

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

        # data = {'info': 'super puper info'}
        #
        # new_info = HostInfo(info=data['info'])
        # db.session.add(new_info)
        # db.session.commit()

        res = {'message': 'playbook running...'}
        return ResponseSchema().dump(res)


class ResponseSchema(ApiSchema):

    # id = fields.Str(default=None)
    message = fields.Str(default=None)
