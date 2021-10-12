from typing import List, Optional

from pydantic import BaseModel


class EntryBase(BaseModel):
    id: int
    value: str


class EntryCreate(EntryBase):
    pass


class Entry(EntryBase):
    id: int
    value: str
    timestamp: int

    class Config:
        orm_mode = True

