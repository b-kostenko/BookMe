from abc import abstractmethod, ABC

from src.domain.enums import TokenType


class AbstractAuthSecurity(ABC):

    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a plain password against a hashed password."""
        raise NotImplementedError

    @abstractmethod
    def hash_password(self, password: str) -> str:
        """Hash a plain password."""
        raise NotImplementedError

    @abstractmethod
    def create_token(self, payload: dict, token_type: TokenType, expire_minutes: int) -> str:
        """Create an access token."""
        raise NotImplementedError

    @abstractmethod
    def decode_token(self, token: str, key: str, options: dict, algorithms: list[str]) -> dict:
        """Decode a token."""
        raise NotImplementedError

    @abstractmethod
    def verify_token(self, token: str, token_type: TokenType) -> bool:
        """Verify a token."""
        raise NotImplementedError