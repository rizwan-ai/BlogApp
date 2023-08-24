pip install fastapi
pip install "uvicorn[standard]"
pip install sqlmodel
pip install asyncpg
pip install alembic

----------------
FastAPI, SQLModel

- Asyncpg  -- PostgreSQL
- Alembic  -- Database Migration Toolkit

------------------------------------------

pip freeze > requirements.txt

------------------------------------------

git init

alembic init -t async migrations

alembic revision --autogenerate -m "initial migrations"
alembic upgrade head
