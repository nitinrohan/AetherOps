# app/db.py
from typing import Optional  # typing help
from sqlalchemy import create_engine  # sync engine (ok for SQLite or simple cases)
from sqlalchemy.orm import sessionmaker  # DB session factory
from .settings import settings  # imports our loaded Settings

# create the engine using the DATABASE_URL from the .env file
engine = create_engine(settings.DATABASE_URL, future=True, pool_pre_ping=True)

# create a session factory bound to the engine
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)

def get_db():
    """
    FastAPI dependency that yields a DB session and ensures it's closed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
