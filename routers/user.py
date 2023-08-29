# Importing Python packages

# Importing FastAPI packages
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse

# Importing SQLModel packages
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

# Importing from project files
from core.db import get_session


# Router Object to Create Routes
router = APIRouter(
    prefix="/user",
    tags=["User"],
)

# ----------------------------------------------------------------------------#
