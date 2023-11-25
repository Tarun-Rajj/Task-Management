import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_URL = os.getenv(
    "DB_URL", "sqlite:///./sql_api.db?check_same_thread=False"
)

engine = create_engine(DB_URL, pool_recycle=280, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    # Creates a session query
    db = SessionLocal()
    try:
        # Wait until it's used
        yield db
    finally:
        # Close the connection
        db.close()
