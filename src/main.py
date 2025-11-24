import uvicorn
from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from src.config import settings
from src.domain.exceptions import (
    BusinessRuleViolation,
    InsufficientPermissions,
    InvalidCredentials,
    InvalidOperation,
    ObjectAlreadyExists,
    ObjectNotFound,
    ObjectValidationError,
)
from src.presentation.api import exceptions as exception_handlers
from src.presentation.api.v1.router import api_v1_router as routers



def _include_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def _include_router(app: FastAPI) -> None:
    app.include_router(routers)


def _include_exception_handlers(app: FastAPI) -> None:
    """Register exception handlers for domain exceptions."""
    app.add_exception_handler(
        ObjectNotFound, exception_handlers.handle_object_not_found
    )
    app.add_exception_handler(
        ObjectAlreadyExists, exception_handlers.handle_object_already_exists
    )
    app.add_exception_handler(
        ObjectValidationError, exception_handlers.handle_object_validation_error
    )
    app.add_exception_handler(
        BusinessRuleViolation, exception_handlers.handle_business_rule_violation
    )
    app.add_exception_handler(
        InsufficientPermissions, exception_handlers.handle_insufficient_permissions
    )
    app.add_exception_handler(
        InvalidOperation, exception_handlers.handle_invalid_operation
    )
    app.add_exception_handler(
        InvalidCredentials, exception_handlers.handle_invalid_credentials
    )


def create_app() -> FastAPI:
    app = FastAPI()
    _include_middleware(app)
    _include_exception_handlers(app)
    _include_router(app)

    return app


if __name__ == "__main__":
    uvicorn.run("main:create_app", host=settings.HOST, port=settings.PORT)
