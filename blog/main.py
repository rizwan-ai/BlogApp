# Main FastAPI app     blog/main.py

from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication

app = FastAPI()

# Create the database table
models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/blog", status_code=status.HTTP_201_CREATED, tags=["blogs"])
# async def create(blog: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
# async def destroy(id, db: Session = Depends(get_db)):
#     blogi = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blogi.first():
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
#         )
#     blogi.delete(synchronize_session=False)
#     db.commit()
#     return "done"


# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
# async def update(id, blog: schemas.Blog, db: Session = Depends(get_db)):
#     # print(blog)
#     blogi = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blogi.first():
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
#         )
#     print(type(blogi))
#     blogi.update(blog.dict())

#     db.commit()
#     return "updated"


# @app.get("/blog", response_model=list[schemas.ShowBlog], tags=["blogs"])
# async def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog, tags=["blogs"])
# async def show(id, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Blog with the id {id} is not available",
#         )
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"detail": f"Blog with the id {id} is not avialable"}
#     return blog


# @app.post("/user", response_model=schemas.ShowUser, tags=["users"])
# def create_user(user: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(
#         name=user.name, email=user.email, password=Hash.bcrypt(user.password)
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get("/user/{id}", response_model=schemas.ShowUser, tags=["users"])
# async def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with the id {id} is not available",
#         )
#     return user
