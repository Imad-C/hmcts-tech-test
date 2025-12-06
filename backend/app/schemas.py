from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from .utils import Status

class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: Optional[str] = None
    status: Status
    due: datetime

class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    status: Status
    due: datetime

    class Config:
        from_attributes = True