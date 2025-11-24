"""Business logic exceptions.

These exceptions represent violations of business rules and domain constraints.
"""

from src.domain.exceptions.base import DomainException


class BusinessRuleViolation(DomainException):
    """Raised when a business rule is violated.
    
    Example:
        raise BusinessRuleViolation("Cannot book appointment in the past")
    """
    pass


class InsufficientPermissions(DomainException):
    """Raised when a user lacks required permissions.
    
    Example:
        raise InsufficientPermissions("User cannot cancel this appointment")
    """
    pass


class InvalidOperation(DomainException):
    """Raised when an operation is invalid in the current context.
    
    Example:
        raise InvalidOperation("Cannot reschedule a completed appointment")
    """
    pass

