from fastapi import APIRouter

from src.config import settings

router = APIRouter(tags=["Health"])


@router.get("/health", summary="Health check")
async def health_check():
    """Health check endpoint to verify that the application is running."""
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }