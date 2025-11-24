"""Authentication and authorization exceptions."""

from src.domain.exceptions.base import DomainException


class InvalidCredentials(DomainException):
    """Raised when authentication credentials are invalid.
    
    Example:
        raise InvalidCredentials("Invalid email or password")
    """
    pass

