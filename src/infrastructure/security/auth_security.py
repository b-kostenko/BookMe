from datetime import datetime, timedelta, timezone

import bcrypt
import jwt

from src.application.interfaces.auth_security import AbstractAuthSecurity
from src.config import settings
from src.domain.enums import TokenType
from src.domain.exceptions import InvalidCredentials


class AuthSecurity(AbstractAuthSecurity):
    """Security service for password hashing and token management."""

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a plain password against a hashed password.
        
        Args:
            plain_password: Plain text password
            hashed_password: Hashed password (bcrypt format)
            
        Returns:
            True if password matches, False otherwise
        """
        return bcrypt.checkpw(
            plain_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )

    def hash_password(self, password: str) -> str:
        """Hash a plain password using bcrypt.
        
        Args:
            password: Plain text password
            
        Returns:
            Hashed password string
        """
        # Generate salt and hash password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def create_token(self, payload: dict, token_type: TokenType, expire_minutes: int) -> str:
        to_encode = payload.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
        to_encode.update({"exp": expire, "type": token_type})
        return jwt.encode(to_encode, settings.token.SECRET_KEY, algorithm=settings.token.ALGORITHM)

    def decode_token(self, token: str, key: str, options: dict, algorithms: list[str]) -> dict:
        try:
            payload = jwt.decode(jwt=token, key=key, algorithms=algorithms, options=options)
            return payload
        except jwt.ExpiredSignatureError:
            raise InvalidCredentials("Token has expired")
        except (jwt.InvalidTokenError, jwt.DecodeError):
            raise InvalidCredentials("Invalid token")

    def verify_token(self, token: str, token_type: TokenType) -> bool:
        try:
            payload = self.decode_token(
                token=token, key=settings.token.SECRET_KEY, algorithms=[settings.token.ALGORITHM], options={}
            )

            if payload.get("type") != token_type.value:
                raise InvalidCredentials("Invalid token type")
            return True

        except InvalidCredentials:
            return False
        except ValueError:
            return False
