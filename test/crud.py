from sqlalchemy.orm import Session
from . import models, schemas

def create_entry(db: Session, entry: schemas.EntryCreate):
    db_entry = models.Entry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_entry(db: Session, entry_id: int):
    return db.query(models.Entry).filter(models.Entry.id == entry_id).first()

def get_entries(db: Session, skip=0, limit=100):
    return db.query(models.Entry).offset(skip).limit(limit).all()

def update_entry(db: Session, entry_id: int, update_data: schemas.EntryUpdate):
    db_entry = get_entry(db, entry_id)
    if db_entry:
        for key, value in update_data.dict().items():
            setattr(db_entry, key, value)
        db.commit()
        db.refresh(db_entry)
    return db_entry

def delete_entry(db: Session, entry_id: int):
    db_entry = get_entry(db, entry_id)
    if db_entry:
        db.delete(db_entry)
        db.commit()
    return db_entry
