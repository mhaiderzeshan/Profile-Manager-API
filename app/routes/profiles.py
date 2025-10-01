from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter(
    prefix="/profiles",
    tags=["/profiles"]
)


@router.post("/create_profile", response_model=schemas.Profile)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    return crud.create_profile(db=db, profile=profile)


@router.get("/", response_model=list[schemas.ProfileBase])
def get_profiles(db: Session = Depends(get_db)):
    return crud.get_profiles(db=db)


@router.get("/{profile_id}", response_model=schemas.Profile)
def get_profile_by_id(profile_id: int, db: Session = Depends(get_db)):
    db_profile = crud.get_profile_by_id(db, profile_id=profile_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile


@router.put("/{profile_id}", response_model=schemas.Profile)
def update_profile(profile_id: int, profile: schemas.ProfileUpdate, db: Session = Depends(get_db)):
    db_profile = crud.update_profile(
        db=db, profile_id=profile_id, profile=profile)

    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    return db_profile


@router.delete("/{profile_id}", response_model=schemas.Profile)
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    db_profile = crud.delete_profile(profile_id=profile_id, db=db)

    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    return db_profile
