import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class BackendLogs(BaseModel):
    id: Optional[str] = Field(alias='_id', default_factory=lambda: str(ObjectId()))
    route_action: str
    domain: str
    client_host: str
    city: str
    content: str
    datum_vnosa: datetime.datetime = Field(default_factory=datetime.datetime.now)
