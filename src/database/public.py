import datetime

from src.domain.public import LoggingPublic

logging_public = [
    LoggingPublic(
        route_action='route_action',
        domain='PUBLIC',
        content='All blog Loaded Client. Device is: Desktop',
        client_host='localhost',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
