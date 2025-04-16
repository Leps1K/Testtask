from pydantic import BaseModel
from datetime import datetime

class EntryBase(BaseModel):
    title: str
    content: str | None = None

class EntryCreate(EntryBase):
    pass

class EntryUpdate(EntryBase):
    is_done: bool

class EntryOut(EntryBase):
    id: int
    created_at: datetime
    is_done: bool

    class Config:
        orm_mode = True
