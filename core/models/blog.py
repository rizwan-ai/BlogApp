from sqlmodel import Field, SQLModel
from constants import SCHEMA, TABLE_BLOG

# class BaseBlog(SQLModel):
#     name: str
#     description: str
#     author: str


class Blog(SQLModel, table=True):
    __table_args__ = {"schema": SCHEMA}
    __tablename__ = TABLE_BLOG

    id: int | None = Field(default=None, primary_key=True)

    name: str
    description: str
    author: str
