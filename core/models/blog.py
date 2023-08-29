from sqlmodel import Field, SQLModel
from constants import SCHEMA, TABLE_BLOG


class BaseBlog(SQLModel):
    name: str
    description: str
    author: str


class Blog(BaseBlog, table=True):
    __table_args__ = {"schema": SCHEMA}
    __tablename__ = TABLE_BLOG

    id: int | None = Field(default=None, primary_key=True)


class CreateBlog(BaseBlog):
    pass


class UpdateBlog(BaseBlog):
    pass


class DeleteBlog(BaseBlog):
    pass
