from src.application.interfaces.auth_security import AbstractAuthSecurity
from src.application.interfaces.user_repository import AbstractUserRepository
from src.application.schemas.user import UserInputSchema, UserOutputSchema
from src.domain.entities.domainuser import DomainUser
from src.domain.exceptions import ObjectAlreadyExists


class UserService:
    """Service for user-related business logic.
    
    This service belongs to the application layer and orchestrates
    domain entities and repository operations.
    """
    
    def __init__(self, user_repository: AbstractUserRepository, auth_security: AbstractAuthSecurity):
        self.user_repository: AbstractUserRepository = user_repository
        self.auth_security: AbstractAuthSecurity = auth_security

    async def create_user(self, user_input: UserInputSchema) -> UserOutputSchema:
        """Create a new user.
        
        Args:
            user_input: User input data from the presentation layer
            
        Returns:
            User output schema with created user data
            
        Raises:
            ObjectAlreadyExists: If user with this email already exists
        """
        # Check if user already exists
        existing_user = await self.user_repository.get_user(email=user_input.email)
        if existing_user:
            raise ObjectAlreadyExists(f"User with this email: {user_input.email} already exists.")

        # Hash password
        password_hash = self.auth_security.hash_password(user_input.password)

        # Create domain entity using factory method
        user = DomainUser.create(
            email=user_input.email,
            phone=user_input.phone,
            password_hash=password_hash,
            first_name=user_input.first_name,
            last_name=user_input.last_name,
        )

        # Save through repository (returns domain entity with timestamps)
        created_user = await self.user_repository.create_user(user)

        # Convert domain entity to output schema
        return UserOutputSchema.model_validate(created_user.to_dict())
