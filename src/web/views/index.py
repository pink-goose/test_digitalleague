from flask import (
    render_template,
)

from models import (
    HostInfo,
)


def index():
    infos = HostInfo.query.all()

    items = [
        {
            'cluster': info.cluster,
            'host': info.host,
            'info': info.info,
            'created_date': info.created_date
        }
        for info in infos
    ]

    return render_template('index.html', items=items)
