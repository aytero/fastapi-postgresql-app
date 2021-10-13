from sqlalchemy import Column, Integer, String

from .database import Base


class Entry(Base):
    __tablename__ = "entries_db"

    id = Column(Integer, primary_key=True)
    value = Column(String)
    timestamp = Column(Integer)
