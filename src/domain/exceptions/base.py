"""Base exception classes for the domain layer."""


class DomainException(Exception):
    """Base exception for all domain-related errors.
    
    This is the root exception class for all custom domain exceptions.
    All domain exceptions should inherit from this class.
    """
    
    def __init__(self, message: str):
        """Initialize domain exception.
        
        Args:
            message: Human-readable error message
        """
        super().__init__(message)
        self.message = message

