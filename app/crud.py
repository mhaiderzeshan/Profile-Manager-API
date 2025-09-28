from sqlalchemy.orm import Session
from app import models, schemas


# create profile
def create_profile(db: Session, profile: schemas.ProfileCreate):
    db_profile = models.Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile  

# get all profiles
def get_profiles(db: Session):
    return db.query(models.Profile)

# get profile by id
def get_profile_by_id(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()

# update profile
def update_profile(profile_id: int, db: Session, profile: schemas.ProfileUpdate):
    db_profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()

    if not db_profile:
        return None
    
    # update only provided fields
    for key, value in profile.dict().items():
        setattr(db_profile, key, value)

    db.commit()
    db.refresh(db_profile)
    return db_profile


# delete profile
def delete_profile(profile_id: int, db: Session):
    db_profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if not db_profile:
        return None
    
    db.delete(db_profile)
    db.commit()

    return db_profile