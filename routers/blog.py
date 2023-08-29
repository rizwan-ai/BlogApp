# Importing Python packages
import traceback

# Importing FastAPI packages
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse

# Importing SQLModel packages
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

# Importing from project files
from core.db import get_session
from core.models.blog import Blog, CreateBlog


# Router Object to Create Routes
router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
)

# ----------------------------------------------------------------------------#


# Create Blog
@router.post("/", summary="Create Blog")
async def create_blog(blog: CreateBlog, session: AsyncSession = Depends(get_session)):
    try:
        blog_data = Blog(
            name=blog.name, description=blog.description, author=blog.author
        )
        session.add(blog_data)
        await session.commit()
        await session.refresh(blog_data)

        # response = JSONResponse(
        #     status_code=status.HTTP_201_CREATED,
        #     content={"message": "Blog Created Successfully", "data": blog_data},
        # )
        return {"blog": blog_data}

    except HTTPException as http_exception:
        print("http_exception --> ", http_exception)
        raise http_exception
    except Exception as ex:
        exception_list = traceback.format_exc()
        exception_list += "\n\n"
        exception_list += str(ex)
        print("Exception --> ", exception_list)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error",
        ) from ex


# Get All Blogs
@router.get("/", summary="Get All Blogs")
async def get_all_blogs(session: AsyncSession = Depends(get_session)):
    try:
        result = await session.execute(select(Blog))
        blogs = result.scalars().all()

        response_data = {"blogs": blogs}

        # response = JSONResponse(
        #     status_code=status.HTTP_200_OK,
        #     content={
        #         "message": "All Blogs Fetched Successfully",
        #         "data": response_data,
        #     },
        # )
        return response_data

    except HTTPException as http_exception:
        print("http_exception --> ", http_exception)
        raise http_exception
    except Exception as ex:
        exception_list = traceback.format_exc()
        exception_list += "\n\n"
        exception_list += str(ex)
        print("Exception --> ", exception_list)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error",
        ) from ex


# Get Blog By ID
@router.get("/{blog_id}", summary="Get Blog By ID")
async def get_blog_by_id(blog_id: int, session: AsyncSession = Depends(get_session)):
    try:
        result = await session.execute(select(Blog).where(Blog.id == blog_id))
        blog = result.scalars().first()

        if not blog:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with ID {blog_id} not found",
            )

        response_data = {"blog": blog}

        # response = JSONResponse(
        #     status_code=status.HTTP_200_OK,
        #     content={
        #         "message": f"Blog with ID {blog_id} Fetched Successfully",
        #         "data": response_data,
        #     },
        # )
        return response_data

    except HTTPException as http_exception:
        print("http_exception --> ", http_exception)
        raise http_exception
    except Exception as ex:
        exception_list = traceback.format_exc()
        exception_list += "\n\n"
        exception_list += str(ex)
        print("Exception --> ", exception_list)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error",
        ) from ex


# Delete Blog By ID
@router.delete("/{blog_id}", summary="Delete Blog By ID")
async def delete_blog_by_id(blog_id: int, session: AsyncSession = Depends(get_session)):
    try:
        result = await session.execute(select(Blog).where(Blog.id == blog_id))
        blog = result.scalars().first()

        if not blog:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with ID {blog_id} not found",
            )

        await session.delete(blog)
        await session.commit()

        # response = JSONResponse(
        #     status_code=status.HTTP_200_OK,
        #     content={
        #         "message": f"Blog with ID {blog_id} Deleted Successfully",
        #         "data": None,
        #     },
        # )
        return {"message": f"Blog with ID {blog_id} Deleted Successfully"}

    except HTTPException as http_exception:
        print("http_exception --> ", http_exception)
        raise http_exception
    except Exception as ex:
        exception_list = traceback.format_exc()
        exception_list += "\n\n"
        exception_list += str(ex)
        print("Exception --> ", exception_list)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error",
        ) from ex


# Update Blog By ID
@router.put("/{blog_id}", summary="Update Blog By ID")
async def update_blog_by_id(
    blog_id: int, blog: CreateBlog, session: AsyncSession = Depends(get_session)
):
    try:
        result = await session.execute(select(Blog).where(Blog.id == blog_id))
        blog_data = result.scalars().first()

        if not blog_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with ID {blog_id} not found",
            )

        blog_data.name = blog.name
        blog_data.description = blog.description
        blog_data.author = blog.author

        await session.commit()
        await session.refresh(blog_data)

        # response = JSONResponse(
        #     status_code=status.HTTP_200_OK,
        #     content={
        #         "message": f"Blog with ID {blog_id} Updated Successfully",
        #         "data": blog_data,
        #     },
        # )
        return {"blog": blog_data}

    except HTTPException as http_exception:
        print("http_exception --> ", http_exception)
        raise http_exception
    except Exception as ex:
        exception_list = traceback.format_exc()
        exception_list += "\n\n"
        exception_list += str(ex)
        print("Exception --> ", exception_list)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error",
        ) from ex
