from sqlalchemy.orm import Session
from .. import models, db
from pydantic import EmailStr


def get_user(db: Session, email: EmailStr):
    return db.query(models.User).filter(models.User.email == email).first()


