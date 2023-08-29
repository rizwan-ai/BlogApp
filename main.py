# Importing Python packages

# Importing FastAPI packages
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.responses import JSONResponse

# Importing SQLModel packages
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

# Importing from project files
from core.db import get_session
from core.models.blog import Blog, CreateBlog


# Router Object to Create Routes
app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    title="Blog APIs",
    description="BlogApp API Documentation",
    version="0.1a",
)

# ----------------------------------------------------------------------------#


@app.get("/")
def root():
    return {"message": "Hey, My BlogApp is Running"}


# CRUD Operations BlogApp


@app.post("/blog")
async def create_blog(blog: CreateBlog, session: AsyncSession = Depends(get_session)):
    blog_data = Blog(name=blog.name, description=blog.description, author=blog.author)
    session.add(blog_data)
    await session.commit()
    await session.refresh(blog_data)

    response = JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Blog Created Successfully", "data": blog_data},
    )
    return response


@app.get("/blog")
async def get_all_blogs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Blog))
    blogs = result.scalars().all()

    response_data = {"blogs": blogs}

    # response = JSONResponse(
    #     status_code=status.HTTP_200_OK,
    #     content={"message": "All Blogs Fetched Successfully", "data": response_data},
    # )
    return response_data


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5000)
