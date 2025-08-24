from sqlalchemy.orm import Session
from . import models

def create_user(db: Session, name: str):
    db_user = models.User(name=name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()
