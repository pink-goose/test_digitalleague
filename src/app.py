from flask import Flask
from extensions import (
    init_cors,
    init_postgresql,
)


def create_app():
    app = Flask(__name__, static_folder='web/static', static_url_path='')
    app.config.from_object('config')

    init_extensions(app)
    init_blueprints(app)

    return app


def init_extensions(app):
    init_cors(app)
    init_postgresql(app)


def init_blueprints(app):
    from api.routes import api_bp
    from web.routes import web_bp

    app.register_blueprint(api_bp)
    app.register_blueprint(web_bp)


if __name__ == '__main__':
    create_app().run(host='0.0.0.0')
