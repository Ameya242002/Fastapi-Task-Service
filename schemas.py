from pydantic import BaseModel
from typing import Optional
import datetime

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: Optional[int] = None
    # user_id: int


class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    is_completed: Optional[bool]

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    is_completed: bool
    user_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True
