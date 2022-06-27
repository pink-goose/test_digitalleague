from sqlalchemy.sql import func
from extensions.postgresql import db


class HostInfo(db.Model):
    __tablename__ = 'hosts_info'

    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String())
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    cluster = db.Column(db.String())
    host = db.Column(db.String())

    def __init__(self, cluster, host, info):
        self.cluster = cluster
        self.host = host
        self.info = info
        # self.created_date = created_date

    def __repr__(self):
        return f""
