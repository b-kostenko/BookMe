from abc import ABC, abstractmethod

from src.domain.entities.domainuser import DomainUser


class AbstractUserRepository(ABC):
    """Repository interface for User domain entity.
    
    This interface is defined in the application layer but works with domain entities.
    The implementation will be in the infrastructure layer.
    """
    
    @abstractmethod
    async def create_user(self, user: DomainUser) -> DomainUser:
        """Create a new user in the repository.
        
        Args:
            user: User domain entity to create
            
        Returns:
            Created User domain entity with generated ID and timestamps
        """
        raise NotImplementedError

    @abstractmethod
    async def get_user(self, email: str) -> DomainUser | None:
        """Retrieve a user by email.
        
        Args:
            email: User email address
            
        Returns:
            User domain entity if found, None otherwise
        """
        raise NotImplementedError
