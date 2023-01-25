from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config import config

engine = create_async_engine(config.database_uri())
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = async_session_maker()
    try:
        yield session
    except:
        await session.rollback()
    finally:
        await session.close()

with_session = asynccontextmanager(get_async_session)

Base = declarative_base()
