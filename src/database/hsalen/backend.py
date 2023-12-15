import datetime

from src.domain.hsalen.backend import BackendLogs

backend_logs = [
    BackendLogs(
        route_action='route_path',
        domain='BACKEND',
        content='content',
        client_host='84.52.156.154',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
