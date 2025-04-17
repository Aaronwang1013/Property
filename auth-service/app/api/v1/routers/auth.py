from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.schema import user as user_schema
from app.models import user as user_model
from app.db.session import get_db
from app.core.security import create_access_token
from app.config import settings

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


@router.post("/register", response_model=user_schema.UserResponse)
def register_user(
    user: user_schema.UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = (
        db.query(user_model.User).filter(user_model.User.email == user.email).first()
    )
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashd_pw = hash_password(user.password)
    new_user = user_model.User(email=user.email, hashed_password=hashd_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login", response_model=user_schema.Token)
def login_user(
    credentials: user_schema.UserLogin,
    db: Session = Depends(get_db),
):
    user = (
        db.query(user_model.User)
        .filter(user_model.User.email == credentials.email)
        .first()
    )
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}


