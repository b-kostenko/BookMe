"""Exception handlers for FastAPI application.

This module contains exception handlers that convert domain exceptions
into appropriate HTTP responses.
"""

from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.domain.exceptions import (
    BusinessRuleViolation,
    InsufficientPermissions,
    InvalidCredentials,
    InvalidOperation,
    ObjectAlreadyExists,
    ObjectNotFound,
    ObjectValidationError,
)


def handle_object_not_found(_: Request, e: ObjectNotFound) -> JSONResponse:
    """Handle ObjectNotFound exception."""
    return JSONResponse(
        content={"message": str(e)},
        status_code=status.HTTP_404_NOT_FOUND,
    )


def handle_object_already_exists(_: Request, e: ObjectAlreadyExists) -> JSONResponse:
    """Handle ObjectAlreadyExists exception."""
    return JSONResponse(
        content={"message": str(e)},
        status_code=status.HTTP_409_CONFLICT,
    )


def handle_object_validation_error(
    _: Request, e: ObjectValidationError
) -> JSONResponse:
    """Handle ObjectValidationError exception."""
    return JSONResponse(
        content={"message": str(e)},
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


def handle_business_rule_violation(
    _: Request, e: BusinessRuleViolation
) -> JSONResponse:
    """Handle BusinessRuleViolation exception."""
    return JSONResponse(
        content={"message": str(e)},
        status_code=status.HTTP_400_BAD_REQUEST,
    )


def handle_insufficient_permissions(
    _: Request, e: InsufficientPermissions
) -> JSONResponse:
    """Handle InsufficientPermissions exception."""
    return JSONResponse(
        content={"message": str(e)},
        status_code=status.HTTP_403_FORBIDDEN,
    )


def handle_invalid_operation(_: Request, e: InvalidOperation) -> JSONResponse:
    """Handle InvalidOperation exception."""
    return JSONResponse(
        content={"message": str(e)},
        status_code=status.HTTP_400_BAD_REQUEST,
    )


def handle_invalid_credentials(_: Request, e: InvalidCredentials) -> JSONResponse:
    """Handle InvalidCredentials exception."""
    return JSONResponse(
        content={"message": str(e)},
        status_code=status.HTTP_401_UNAUTHORIZED,
    )

