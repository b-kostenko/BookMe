from fastapi import APIRouter
from src.presentation.api.v1.endpoints import health

api_v1_router = APIRouter(prefix="/v1")


api_v1_router.include_router(health.router)
