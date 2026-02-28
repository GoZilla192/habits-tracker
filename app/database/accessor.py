from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.settings import Settings

engine = create_engine(Settings().sqlite_db_url)
session_factory = sessionmaker(bind=engine)

def get_db_session() -> Session:
	return session_factory
