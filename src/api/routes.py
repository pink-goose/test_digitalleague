from flask import Blueprint
from rest_core import Api
from .resources.ansible import (
    RunAnsiblePlaybook,
)
from .resources.info import (
    InfoGet,
    InfosGet,
    InfoRunUpdate,
)
from .resources.ping import (
    Ping,
)


api_bp = Blueprint('api', __name__, url_prefix='/v1.0', template_folder='./templates')

api = Api(api_bp)


api.add_resource(RunAnsiblePlaybook, '/run_playbook')
# api.add_resource(RunAnsiblePlaybook, '/run')
api.add_resource(InfoRunUpdate, '/info')
api.add_resource(InfosGet, '/info')
api.add_resource(InfoGet, '/info/<string:info_id>')
api.add_resource(Ping, '/ping')
