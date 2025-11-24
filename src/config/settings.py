from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent.parent

class DatabaseSettings(BaseSettings):
    """Database connection settings."""

    POSTGRES_DRIVER: str = Field(default="postgresql+asyncpg", alias="POSTGRES_DRIVER")
    POSTGRES_USER: str = Field(..., alias="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., alias="POSTGRES_PASSWORD")
    POSTGRES_HOST: str = Field(..., alias="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(default=5432, alias="POSTGRES_PORT")
    POSTGRES_DB: str = Field(..., alias="POSTGRES_DB")

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_prefix="POSTGRES_", extra="ignore")

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"{self.POSTGRES_DRIVER}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


class Settings(BaseSettings):
    """Application settings loaded from environment variables and a .env file."""

    # ========== Application ==========
    APP_NAME: str = "FastAPI Onion App"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    database: DatabaseSettings = DatabaseSettings()

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


settings = Settings()
