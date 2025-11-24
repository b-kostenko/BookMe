from datetime import time, datetime
from uuid import UUID
from pydantic import EmailStr

from sqlalchemy import Enum, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.enums import StaffMemberRole, AppointmentStatus, WeekDay
from src.infrastructure.database import BaseModelMixin


class User(BaseModelMixin):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[EmailStr] = mapped_column(String(100), unique=True)
    phone: Mapped[str] = mapped_column(String(25))
    password_hash: Mapped[str] = mapped_column(String(500))

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"


class Review(BaseModelMixin):
    __tablename__ = "reviews"

    staff_id: Mapped[UUID] = mapped_column(ForeignKey("staff.id", ondelete="CASCADE"))
    appointment_id: Mapped[UUID] = mapped_column(ForeignKey("appointments.id", ondelete="CASCADE"))

    rating: Mapped[float] = mapped_column()
    comment: Mapped[str | None] = mapped_column(String(500))

    # Relations
    staff: Mapped["Staff"] = relationship("Staff", back_populates="reviews")
    appointment: Mapped["Appointment"] = relationship("Appointment", back_populates="reviews")

    def __repr__(self):
        return f"<Review(id={self.id}, rating={self.rating})>"


class Company(BaseModelMixin):
    __tablename__ = "companies"

    company_name: Mapped[str] = mapped_column(String(100))
    company_address: Mapped[str] = mapped_column(String(200))
    company_email: Mapped[EmailStr | None] = mapped_column(String(200))
    company_phone: Mapped[str | None] = mapped_column(String(25))
    company_logo_url: Mapped[str | None] = mapped_column(String(200))

    # Relations
    staff: Mapped[list["Staff"]] = relationship(
        back_populates="company",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self):
        return f"<Company(id={self.id}, name='{self.company_name}')>"


class Staff(BaseModelMixin):
    __tablename__ = "staff"

    avatar_url: Mapped[str | None] = mapped_column(String(200))

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    company_id: Mapped[UUID] = mapped_column(ForeignKey("companies.id", ondelete="CASCADE"))

    role: Mapped[StaffMemberRole] = mapped_column(
        Enum(StaffMemberRole, name="staff_role_enum", native_enum=True),
        default=StaffMemberRole.MEMBER,
        nullable=False
    )

    # Relations
    user: Mapped["User"] = relationship("User", back_populates="staff_memberships")
    company: Mapped["Company"] = relationship("Company", back_populates="staff")
    services: Mapped[list["StaffService"]] = relationship(back_populates="staff", cascade="all, delete-orphan",
                                                          passive_deletes=True)
    appointments: Mapped[list["Appointment"]] = relationship(back_populates="staff", cascade="all, delete-orphan",
                                                             passive_deletes=True)
    reviews: Mapped[list["Review"]] = relationship(back_populates="staff", cascade="all, delete-orphan",
                                                   passive_deletes=True)
    working_hours: Mapped[list["WorkingHours"]] = relationship(back_populates="staff", cascade="all, delete-orphan",
                                                               passive_deletes=True)

    __table_args__ = (
        UniqueConstraint("user_id", "company_id", name="uq_user_company"),
    )

    def __repr__(self):
        return f"<Staff(id={self.id}, user_id={self.user_id}, company_id={self.company_id}, role='{self.role}')>"


class StaffService(BaseModelMixin):
    __tablename__ = "staff_services"

    staff_id: Mapped[UUID] = mapped_column(ForeignKey("staff.id", ondelete="CASCADE"))

    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(String(500))
    price: Mapped[float] = mapped_column()
    duration: Mapped[int] = mapped_column(comment="Duration of the service in minutes")
    is_active: Mapped[bool] = mapped_column(default=True)

    # Relations
    staff: Mapped["Staff"] = relationship("Staff", back_populates="services")

    def __repr__(self):
        return f"<StaffService(id={self.id}, name='{self.name}', price={self.price})>"


class Appointment(BaseModelMixin):
    __tablename__ = "appointments"

    company_id: Mapped[UUID] = mapped_column(ForeignKey("companies.id", ondelete="CASCADE"))
    staff_id: Mapped[UUID] = mapped_column(ForeignKey("staff.id", ondelete="SET NULL"), nullable=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    service_id: Mapped[UUID] = mapped_column(ForeignKey("staff_services.id", ondelete="SET NULL"), nullable=True)

    appointment_start: Mapped[datetime] = mapped_column()
    appointment_end: Mapped[datetime] = mapped_column()
    status: Mapped[AppointmentStatus] = mapped_column(
        Enum(AppointmentStatus, name="appointment_status", native_enum=True),
        default=AppointmentStatus.SCHEDULED,
        nullable=False
    )

    # Relations
    company: Mapped["Company"] = relationship("Company", back_populates="appointments")
    staff: Mapped["Staff"] = relationship("Staff", back_populates="appointments")
    user: Mapped["User"] = relationship("User", back_populates="appointments")
    service: Mapped["StaffService"] = relationship("StaffService", back_populates="appointments")

    def __repr__(self):
        return f"<Appointment(id={self.id}, start={self.appointment_start}, end={self.appointment_end}, status='{self.status}')>"


class WorkingHours(BaseModelMixin):
    __tablename__ = "working_hours"

    staff_id: Mapped[UUID] = mapped_column(ForeignKey("staff.id", ondelete="CASCADE"))
    day_of_week: Mapped[WeekDay] = mapped_column(
        Enum(WeekDay, name="weekday_enum", native_enum=True),
        nullable=False
    )
    start_time: Mapped[time] = mapped_column(comment="Start time of working hours")
    end_time: Mapped[time] = mapped_column(comment="End time of working hours")

    # Relations
    staff: Mapped["Staff"] = relationship("Staff", back_populates="working_hours")

    __table_args__ = (
        UniqueConstraint("staff_id", "day_of_week", name="uq_staff_day_of_week"),
    )

    def __repr__(self):
        return f"<WorkingHours(id={self.id}, staff_id={self.staff_id}, day_of_week={self.day_of_week}, start_time={self.start_time}, end_time={self.end_time})>"
