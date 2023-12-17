import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class GeoData(BaseModel):
    id: Optional[str] = Field(alias='_id', default_factory=lambda: str(ObjectId()))
    ip: str
    city: str
    region: str
    country: str
    loc: str
    org: str
    datum_vnosa: datetime.datetime = Field(default_factory=datetime.datetime.now)
