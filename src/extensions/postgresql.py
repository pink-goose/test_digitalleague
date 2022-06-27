from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = None


def init_postgresql(app):
    global db
    db = SQLAlchemy()
    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db)
    return
