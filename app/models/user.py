from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
from app.db.database import Base
import uuid
import enum


class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    DOCTOR = "DOCTOR"
    PATIENT = "PATIENT"


class User(Base):
    __tablename__ = "users"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String,
        nullable=False
    )

    role = Column(
        Enum(UserRole),
        nullable=False
    )

    patient = relationship(
        "Patient",
        back_populates="user",
        uselist=False
    )

    doctor = relationship(
        "Doctor",
        back_populates="user",
        uselist=False
    )