from fastapi import APIRouter
from src.presentation.api.v1.endpoints import health, user

api_v1_router = APIRouter(prefix="/v1")


api_v1_router.include_router(health.router)
api_v1_router.include_router(user.router)
