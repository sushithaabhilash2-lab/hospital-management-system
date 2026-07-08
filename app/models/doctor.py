from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String,
        nullable=False
    )

    specialization = Column(
        String,
        nullable=False
    )

    experience = Column(
        Integer,
        nullable=False
    )

    phone = Column(
        String,
        nullable=False
    )

    user_id = Column(
        String,
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="doctor"
    )
    appointments = relationship(
    "Appointment",
    back_populates="doctor"
)