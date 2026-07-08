from sqlalchemy.orm import Session

from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate


def create_doctor(
    db: Session,
    doctor: DoctorCreate,
    user_id: str
):
    existing_doctor = (
        db.query(Doctor)
        .filter(Doctor.user_id == user_id)
        .first()
    )

    if existing_doctor:
        return None

    db_doctor = Doctor(
        full_name=doctor.full_name,
        specialization=doctor.specialization,
        experience=doctor.experience,
        phone=doctor.phone,
        user_id=user_id
    )

    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)

    return db_doctor


def get_all_doctors(db: Session):
    return db.query(Doctor).all()


def get_doctor_by_id(
    db: Session,
    doctor_id: int
):
    return (
        db.query(Doctor)
        .filter(Doctor.id == doctor_id)
        .first()
    )


def update_doctor(
    db: Session,
    doctor_id: int,
    doctor: DoctorUpdate
):
    db_doctor = (
        db.query(Doctor)
        .filter(Doctor.id == doctor_id)
        .first()
    )

    if not db_doctor:
        return None

    db_doctor.full_name = doctor.full_name
    db_doctor.specialization = doctor.specialization
    db_doctor.experience = doctor.experience
    db_doctor.phone = doctor.phone

    db.commit()
    db.refresh(db_doctor)

    return db_doctor


def delete_doctor(
    db: Session,
    doctor_id: int
):
    db_doctor = (
        db.query(Doctor)
        .filter(Doctor.id == doctor_id)
        .first()
    )

    if not db_doctor:
        return False

    db.delete(db_doctor)
    db.commit()

    return True