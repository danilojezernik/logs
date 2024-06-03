import datetime

from src.domain.hsalen.private import LoggingPrivate

logging_private = [
    LoggingPrivate(
        route_action='route_action',
        domain='PRIVATE',
        content='content',
        client_host='localhost',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
