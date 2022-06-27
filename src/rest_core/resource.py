from flask import (
    current_app,
    jsonify,
    request,
    g
)
from flask.views import MethodView


class Resource(MethodView):

    # decorators = [format_results]

    @property
    def app(self):
        return current_app

    @property
    def config(self):
        return current_app.config

    @property
    def logger(self):
        return current_app.logger

    @property
    def request(self):
        return request

    # @property
    # def g(self):
    #     return g
