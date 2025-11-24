from fastapi import APIRouter

from src.application.schemas.user import UserOutputSchema, UserInputSchema
from src.presentation.api.dependencies import user_service_deps

router = APIRouter(tags=["User"], prefix="/users")


@router.post("/",response_model=UserOutputSchema ,summary="Create a new user")
async def create_user(user_input: UserInputSchema, user_service: user_service_deps):
    """Endpoint to create a new user."""
    user = await user_service.create_user(user_input=user_input)
    return user