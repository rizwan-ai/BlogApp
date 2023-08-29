# Importing FastAPI packages
from fastapi import APIRouter

# Importing from project files
from routers import blog
from routers import user

# Router Object to Create Routes
router = APIRouter()

# ----------------------------------------------------------------------------#

router.include_router(blog.router)
router.include_router(user.router)
