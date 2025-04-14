from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends
from pydantic import PostgresDsn
from app.core.config import settings

database_url = PostgresDsn.build(
    scheme="postgresql",
    user=settings.db_usr,
    password=settings.db_pwd,
    host=settings.db_host,
    port=f"/{settings.db_port}",
)


SQLALCHEMY_DATABASE_URL = str(database_url)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
