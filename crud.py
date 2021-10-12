from sqlalchemy.orm import Session

from . import models, schemas

import time


def get_entry(db: Session, entry_id: int):
    return db.query(models.Entry).filter(models.Entry.id == entry_id).first()


def get_entry_by_value(db: Session, value: str):
    return db.query(models.Entry).filter(models.Entry.value == value).first()


#entries = crud.get_entries(db, offset=offset, limit=limit, id=id, value=value)
def get_entries(db: Session, offset: int = 0, limit: int = 100, id: int = None, value: str = None):
    query = db.query(models.Entry).offset(offset).limit(limit).all()
    #if id:
    #    query = query.get(id)
    #if value:
    #    query = query.get(value)

    return query
#def get_entries(db: Session, offset: int = 0, limit: int = 100):
#    return db.query(models.Entry).offset(offset).limit(limit).all()

def create_entry(db: Session, entry: schemas.EntryCreate):
    #cur_timestamp = datetime.datetime.now()
    cur_timestamp = time.time() * 1000
    db_entry = models.Entry(id = entry.id, value=entry.value, timestamp=cur_timestamp)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
