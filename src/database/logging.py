import datetime

from src.domain.logging import Logging

logging = [
    Logging(
        route_action='route_action',
        content='content',
        method='POST',
        status_code=200,
        client_host='localhost',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
