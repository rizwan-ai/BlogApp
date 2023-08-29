"""
    Database Connection
    
    Description:
        This module contains the database connection.
"""

# Importing Python packages
from environs import Env

# Importing SQLModel packages
from sqlmodel import create_engine
from sqlmodel.ext.asyncio.session import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker

# ----------------------------------------------------------------------------#


# Creating an instance of the Env class to access environment variables
env = Env()
env.read_env(".env")
# Database connection parameters from environment variables
database = env("DATABASE")
db_username = env("DB_USERNAME")
db_password = env("DB_PASSWORD")
db_host = env("DB_HOST")
db_port = env("DB_PORT")
db_name = env("DB_NAME")
db_schema = env("DB_SCHEMA")


# Database URL for connecting to the PostgreSQL database via the asyncpg driver
db_url = (
    f"{database}+asyncpg://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
)
# Creating an instance of the AsyncEngine class to connect to the database
db_engine = AsyncEngine(create_engine(db_url, echo=True))


async def get_session() -> AsyncSession:
    async_session = sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
