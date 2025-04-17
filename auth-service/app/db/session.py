from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from app.config import settings


def _connection_url() -> str:
    return URL.create(
        drivername="postgresql+psycopg2",
        username=settings.db_usr,
        password=settings.db_pwd,
        host=settings.db_host,
        port=settings.db_port,
        database=settings.db_name,
    )


engine = create_engine(_connection_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
