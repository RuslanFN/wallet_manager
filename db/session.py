from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
import asyncio
from os import getenv
from dotenv import load_dotenv
from typing import AsyncGenerator
load_dotenv()

DB_USER = getenv('DB_USER')
DB_PASS = getenv('DB_PASS')
DB_NAME = getenv('DB_NAME')
DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')

connection_string = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

async_engine = create_async_engine(connection_string)
sessionmaker = async_sessionmaker(async_engine,
                                  expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with sessionmaker() as session:
        yield session
        




