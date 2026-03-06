from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.settings import Settings

settings = Settings()

sync_engine = create_engine(settings.sync_db_url)
async_engine = create_async_engine(settings.async_db_url, future=True, pool_pre_ping=True)

sync_session_factory = sessionmaker(bind=sync_engine, expire_on_commit=False)
async_session_factory = async_sessionmaker(
	async_engine,
	autoflush=False,
	expire_on_commit=False,
)

async def get_sync_db_session() -> Session:
	return sync_session_factory()

async def get_async_db_session() -> AsyncSession:
	async with async_session_factory() as session:
		yield session

