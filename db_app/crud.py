from sqlalchemy.orm import Session
from sqlalchemy import update

from . import models, schemas

from datetime import datetime


def get_entry(db: Session, entry_id: int):
    return db.query(models.Entry).filter(models.Entry.id == entry_id).first()


def get_entries(db: Session, offset: int = 0, limit: int = 100,
                id: int = None, value: str = None, timestamp: int = None):

    query = db.query(models.Entry)
    if id:
        query = query.filter(models.Entry.id == id)
    if value:
        query = query.filter(models.Entry.value == value)
    if timestamp:
        query = query.filter(models.Entry.timestamp == timestamp)
    query = query.offset(offset).limit(limit).all()
    return query
 

def create_entry(db: Session, entry: schemas.EntryCreate):
    curr_dt = datetime.now()
    cur_timestamp = int(round(curr_dt.timestamp()))
    db_entry = models.Entry(id = entry.id, value=entry.value, timestamp=cur_timestamp)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def update_entry(db: Session, entry: schemas.EntryCreate):
    curr_dt = datetime.now()
    cur_timestamp = int(round(curr_dt.timestamp()))
    db.query(models.Entry).filter(models.Entry.id == entry.id).update({'value': entry.value, 'timestamp': cur_timestamp})
    db.commit()
    q = get_entry(db, entry_id=entry.id)
    return q
