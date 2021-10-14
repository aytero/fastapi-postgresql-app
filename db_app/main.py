from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, schemas, models
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create_entry/", response_model=schemas.Entry)
def create_entry(entry: schemas.EntryCreate, db: Session = Depends(get_db)):
    db_entry = crud.get_entry(db, entry_id=entry.id)
    if db_entry:
        raise HTTPException(status_code=400, detail="Entry with this id already exists")
    return crud.create_entry(db=db, entry=entry)


@app.get("/entries/", response_model=List[schemas.Entry])
def read_entries(offset: int = 0, limit: int = 100,
                 id: int = None, value: str = None, timestamp: int = None,
                 db: Session = Depends(get_db)):
    entries = crud.get_entries(db, offset=offset, limit=limit, id=id, value=value, timestamp=timestamp)
    return entries


@app.post("/update_entry/", response_model=schemas.Entry)
def update_entry(entry: schemas.EntryCreate, db: Session = Depends(get_db)):
    db_entry = crud.get_entry(db, entry_id=entry.id)
    if not db_entry:
        raise HTTPException(status_code=400, detail="No entry with this id")
    return crud.update_entry(db=db, entry=entry)
