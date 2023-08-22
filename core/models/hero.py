from sqlmodel import Field, SQLModel
from .constants import SCHEMA, TABLE_HERO


class Hero(SQLModel, table=True):
    __table_args__ = {"schema": SCHEMA}
    __tablename__ = TABLE_HERO

    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
