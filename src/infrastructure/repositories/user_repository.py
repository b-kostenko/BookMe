from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.user_repository import AbstractUserRepository
from src.domain.entities.domainuser import DomainUser
from src.infrastructure.database import User
from src.infrastructure.database.session_manager import provide_async_session


class UserRepository(AbstractUserRepository):
    """Repository implementation for User domain entity.
    
    This class handles the conversion between domain entities and SQLAlchemy models.
    It belongs to the infrastructure layer and implements the application layer interface.
    """

    def _to_domain(self, db_user: User) -> DomainUser:
        """Convert SQLAlchemy model to domain entity.
        
        Args:
            db_user: SQLAlchemy User model
            
        Returns:
            User domain entity
        """
        return DomainUser(
            id=db_user.id,
            email=db_user.email,
            phone=db_user.phone,
            password_hash=db_user.password_hash,
            first_name=db_user.first_name,
            last_name=db_user.last_name,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at,
        )

    def _to_db(self, domain_user: DomainUser) -> User:
        """Convert domain entity to SQLAlchemy model.
        
        Args:
            domain_user: User domain entity
            
        Returns:
            SQLAlchemy User model
        """
        return User(
            id=domain_user.id,
            email=domain_user.email,
            phone=domain_user.phone,
            password_hash=domain_user.password_hash,
            first_name=domain_user.first_name,
            last_name=domain_user.last_name,
        )

    @provide_async_session
    async def create_user(self, user: DomainUser, session: AsyncSession) -> DomainUser:
        """Create a new user in the database.
        
        Args:
            user: User domain entity to create
            session: Database session
            
        Returns:
            Created User domain entity with generated ID and timestamps
        """
        db_user = self._to_db(user)
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return self._to_domain(db_user)

    @provide_async_session
    async def get_user(self, email: str, session: AsyncSession) -> DomainUser | None:
        """Retrieve a user by email.
        
        Args:
            email: User email address
            session: Database session
            
        Returns:
            User domain entity if found, None otherwise
        """
        stmt = select(User).where(User.email == email)
        result = await session.execute(stmt)
        db_user = result.scalar_one_or_none()
        
        if db_user is None:
            return None
        
        return self._to_domain(db_user)