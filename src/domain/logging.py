import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class Logging(BaseModel):
    id: Optional[str] = Field(alias='_id', default_factory=lambda: str(ObjectId()))
    route_action: str
    status_code: int
    client_host: str
    method: str
    content: str
    datum_vnosa: datetime.datetime = Field(default_factory=datetime.datetime.now)
