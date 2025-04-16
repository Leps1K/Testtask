from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/entries/", response_model=schemas.EntryOut)
def create(entry: schemas.EntryCreate, db: Session = Depends(database.get_db)):
    return crud.create_entry(db, entry)

@router.get("/entries/", response_model=list[schemas.EntryOut])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_entries(db, skip, limit)

@router.get("/entries/{entry_id}", response_model=schemas.EntryOut)
def read(entry_id: int, db: Session = Depends(database.get_db)):
    entry = crud.get_entry(db, entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Not found")
    return entry

@router.put("/entries/{entry_id}", response_model=schemas.EntryOut)
def update(entry_id: int, entry: schemas.EntryUpdate, db: Session = Depends(database.get_db)):
    updated = crud.update_entry(db, entry_id, entry)
    if not updated:
        raise HTTPException(status_code=404, detail="Not found")
    return updated

@router.delete("/entries/{entry_id}")
def delete(entry_id: int, db: Session = Depends(database.get_db)):
    deleted = crud.delete_entry(db, entry_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}
