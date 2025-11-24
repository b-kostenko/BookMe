from enum import IntEnum, StrEnum


class WeekDay(IntEnum):
    """Enumeration for days of the week."""
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class TokenType(StrEnum):
    """Enumeration for types of tokens."""
    ACCESS = "access"
    REFRESH = "refresh"