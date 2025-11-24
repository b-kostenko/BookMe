from enum import StrEnum

class AppointmentStatus(StrEnum):
    """Enumeration for the status of an appointment."""
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELED = "canceled"