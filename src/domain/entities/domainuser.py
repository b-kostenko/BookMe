"""User domain entity."""

from datetime import datetime
from uuid import UUID, uuid4


class DomainUser:
    """Domain entity representing a user.
    
    This is a pure domain model without any infrastructure dependencies.
    It represents the business concept of a User in the system.
    """
    
    def __init__(
        self,
        id: UUID,
        email: str,
        phone: str,
        password_hash: str,
        first_name: str | None = None,
        last_name: str | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ):
        """Initialize User entity.
        
        Args:
            id: Unique identifier
            email: User email address
            phone: User phone number
            password_hash: Hashed password
            first_name: User first name (optional)
            last_name: User last name (optional)
            created_at: Creation timestamp
            updated_at: Last update timestamp
        """
        self.id = id
        self.email = email
        self.phone = phone
        self.password_hash = password_hash
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = created_at
        self.updated_at = updated_at
    
    @classmethod
    def create(
        cls,
        email: str,
        phone: str,
        password_hash: str,
        first_name: str | None = None,
        last_name: str | None = None,
    ) -> "DomainUser":
        """Factory method to create a new User entity.
        
        This method generates a new UUID automatically.
        Use this when creating a new user from scratch.
        
        Args:
            email: User email address
            phone: User phone number
            password_hash: Hashed password
            first_name: User first name (optional)
            last_name: User last name (optional)
            
        Returns:
            New DomainUser instance with generated ID
        """
        return cls(
            id=uuid4(),
            email=email,
            phone=phone,
            password_hash=password_hash,
            first_name=first_name,
            last_name=last_name,
        )
    
    def __repr__(self) -> str:
        return f"<User(id={self.id}, email='{self.email}')>"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DomainUser):
            return False
        return self.id == other.id

    def to_dict(self) -> dict:
        """Convert User entity to dictionary."""
        return {
            "id": self.id,
            "email": self.email,
            "phone": self.phone,
            "password_hash": self.password_hash,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
