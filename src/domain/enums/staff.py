from enum import StrEnum


class StaffMemberRole(StrEnum):
    """Enumeration for the roles of staff members."""
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"