from fastapi import APIRouter

from app.core.config import settings
from app.core.logger import logger

router = APIRouter()


@router.get("/health", tags=["Health"])
async def health_check():

    logger.info("Health endpoint called.")

    return {
        "status": "running",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }