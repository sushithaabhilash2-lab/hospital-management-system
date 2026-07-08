from sqlalchemy.orm import Session

from app.models.appointment import Appointment
from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentUpdate
)


def create_appointment(
    db: Session,
    appointment: AppointmentCreate
):
    db_appointment = Appointment(
        appointment_date=appointment.appointment_date,
        appointment_time=appointment.appointment_time,
        reason=appointment.reason,
        patient_id=appointment.patient_id,
        doctor_id=appointment.doctor_id
    )

    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)

    return db_appointment


def get_all_appointments(db: Session):
    return db.query(Appointment).all()


def get_appointment_by_id(
    db: Session,
    appointment_id: int
):
    return (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )


def update_appointment(
    db: Session,
    appointment_id: int,
    appointment: AppointmentUpdate
):
    db_appointment = (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )

    if not db_appointment:
        return None

    db_appointment.appointment_date = appointment.appointment_date
    db_appointment.appointment_time = appointment.appointment_time
    db_appointment.reason = appointment.reason
    db_appointment.patient_id = appointment.patient_id
    db_appointment.doctor_id = appointment.doctor_id

    db.commit()
    db.refresh(db_appointment)

    return db_appointment


def delete_appointment(
    db: Session,
    appointment_id: int
):
    db_appointment = (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )

    if not db_appointment:
        return False

    db.delete(db_appointment)
    db.commit()

    return True