import datetime

from src.domain.hsalen.public import LoggingPublic

logging_public = [
    LoggingPublic(
        route_action='route_action',
        domain='PUBLIC',
        content='content',
        client_host='localhost',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
