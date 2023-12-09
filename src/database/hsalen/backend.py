import datetime

from src.domain.hsalen.backend import BackendLogs

backend_logs = [
    BackendLogs(
        route_action='route_path',
        domain='BACKEND',
        content='content',
        client_host='IPADDRESS',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
