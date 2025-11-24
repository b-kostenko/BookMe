"""Entity-related exceptions."""

from src.domain.exceptions.base import DomainException


class ObjectAlreadyExists(DomainException):
    """Raised when attempting to create an object that already exists.
    
    Example:
        raise ObjectAlreadyExists("User with email already exists")
    """
    pass


class ObjectNotFound(DomainException):
    """Raised when a requested object cannot be found.
    
    Example:
        raise ObjectNotFound("User with id 123 not found")
    """
    pass


class ObjectValidationError(DomainException):
    """Raised when object validation fails.
    
    Example:
        raise ObjectValidationError("Invalid email format")
    """
    pass

