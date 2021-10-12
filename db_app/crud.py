from sqlalchemy.orm import Session
from sqlalchemy import update

from . import models, schemas

import time


def get_entry(db: Session, entry_id: int):
    return db.query(models.Entry).filter(models.Entry.id == entry_id).first()


# not needed
def get_entry_by_value(db: Session, value: str):
    return db.query(models.Entry).filter(models.Entry.value == value).first()


def get_entries(db: Session, offset: int = 0, limit: int = 100,
                id: int = None, value: str = None, timestamp: int = None):

    #if value:
    #    return db.query(models.Entry).filter(models.Entry.value == value).offset(offset).limit(limit).all()
    #if id:
    #    return db.query(models.Entry).filter(models.Entry.id == id).offset(offset).limit(limit).all()
    #return db.query(models.Entry).offset(offset).limit(limit).all()

    query = db.query(models.Entry)
    if id:
        query = query.filter(models.Entry.id == id)
    if value:
        query = query.filter(models.Entry.value == value)
    if timestamp:
        #print(timestamp)
        query = query.filter(models.Entry.timestamp == timestamp)
    query = query.offset(offset).limit(limit).all()
    return query
 

def create_entry(db: Session, entry: schemas.EntryCreate):
    #cur_timestamp = datetime.datetime.now()
    cur_timestamp = time.time() * 1000
    db_entry = models.Entry(id = entry.id, value=entry.value, timestamp=cur_timestamp)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def update_entry(db: Session, entry: schemas.EntryCreate):
    cur_timestamp = time.time() * 1000
    db.query(models.Entry).filter(models.Entry.id == entry.id).update({'value': entry.value, 'timestamp': cur_timestamp})
    db.commit()
    #db.refresh(db_entry)
    return
