from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class User(BaseModel):
    id: Optional[str] = Field(alias='_id', default_factory=lambda: str(ObjectId()))
    username: str
    email: str | None = None
    full_name: str | None = None
    hashed_password: str
    disabled: bool = True
