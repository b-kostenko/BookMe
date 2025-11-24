from enum import Enum
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserInputSchema(BaseModel):
    """Schema for user input data."""

    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr
    phone: str
    password: str

class UserOutputSchema(BaseModel):
    """Schema for user output data."""

    id: UUID
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr
    phone: str

    class Config:
        from_attributes = True
