
from fastapi import APIRouter
from .gerrit import router as gerrit_router

router = APIRouter()

router.include_router(gerrit_router)
