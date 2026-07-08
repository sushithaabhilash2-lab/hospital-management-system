from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    medicine = Column(
        String,
        nullable=False
    )

    dosage = Column(
        String,
        nullable=False
    )

    instructions = Column(
        String,
        nullable=False
    )

    appointment_id = Column(
        Integer,
        ForeignKey("appointments.id"),
        nullable=False
    )

    appointment = relationship(
        "Appointment",
        back_populates="prescriptions"
    )