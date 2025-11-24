"""Domain exceptions module.

This module contains all custom exceptions used in the domain layer.
Exceptions are organized by their purpose and can be imported from here.
"""

from src.domain.exceptions.auth import InvalidCredentials
from src.domain.exceptions.base import DomainException
from src.domain.exceptions.business import (
    BusinessRuleViolation,
    InsufficientPermissions,
    InvalidOperation,
)
from src.domain.exceptions.entity import (
    ObjectAlreadyExists,
    ObjectNotFound,
    ObjectValidationError,
)

__all__ = [
    "DomainException",
    "ObjectAlreadyExists",
    "ObjectNotFound",
    "ObjectValidationError",
    "BusinessRuleViolation",
    "InsufficientPermissions",
    "InvalidOperation",
    "InvalidCredentials",
]

