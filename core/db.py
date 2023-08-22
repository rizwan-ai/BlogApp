"""
    Database Connection
    
    Description:
        This module contains the database connection.
"""

# Importing Python packages
from environs import Env
import asyncio

# Importing SQLModel packages
from sqlmodel import create_engine, SQLModel
from sqlmodel.ext.asyncio.session import AsyncEngine, AsyncSession

# Importing from project files
from models.hero import Hero

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


# testing the model
hero_1 = Hero(name="Imran Khan", secret_name="IK", age=58)
hero_2 = Hero(name="Rizwan", secret_name="D")


async def init_db():
    async with db_engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


# Define an async function to insert heroes into the database
async def insert_heroes():
    async with AsyncSession(db_engine) as session:
        async with session.begin():
            session.add(hero_1)
            session.add(hero_2)
        await session.commit()


async def setup_database():
    await init_db()
    await insert_heroes()


asyncio.run(setup_database())


# psycopg2

# 1. db_engine
# 2. SQLModel.metadata.create_all()
# 3. with Session(engine) as session:
