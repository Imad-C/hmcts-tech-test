from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str
    due: datetime

class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    due: datetime

    class Config:
        from_attributes = True