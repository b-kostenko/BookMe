from typing import Annotated
from fastapi import Depends

from src.application.services.user_service import UserService
from src.infrastructure.repositories.user_repository import UserRepository
from src.infrastructure.security.auth_security import AuthSecurity


def get_user_repository() -> UserRepository:
    return UserRepository()

def get_auth_security() -> AuthSecurity:
    return AuthSecurity()

def get_user_service(
        user_repository: UserRepository = Depends(get_user_repository),
        auth_security: AuthSecurity = Depends(get_auth_security)
) -> UserService:
    return UserService(user_repository=user_repository, auth_security=auth_security)


user_service_deps = Annotated[UserService, Depends(get_user_service)]