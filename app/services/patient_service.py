from sqlalchemy.orm import Session

from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate
from app.core.logger import logger


def create_patient(
    db: Session,
    patient: PatientCreate,
    user_id: str
):
   
    # Check if this user already has a patient profile
    existing_patient = (
        db.query(Patient)
        .filter(Patient.user_id == user_id)
        .first()
    )

    if existing_patient:
        logger.warning(
            "Patient profile already exists for this user."
        )
        return None


    db_patient = Patient(
        full_name=patient.full_name,
        age=patient.age,
        gender=patient.gender,
        phone=patient.phone,
        address=patient.address,
        user_id=user_id
    )

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    logger.info(
    f"Patient created successfully: {db_patient.full_name}"
    )
    return db_patient

def get_all_patients(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    return (
        db.query(Patient)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_patient_by_id(
    db: Session,
    patient_id: int
):
    return (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )


def update_patient(
    db: Session,
    patient_id: int,
    patient: PatientUpdate
):
    db_patient = (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )

    if not db_patient:
        return None

    db_patient.full_name = patient.full_name
    db_patient.age = patient.age
    db_patient.gender = patient.gender
    db_patient.phone = patient.phone
    db_patient.address = patient.address

    db.commit()
    db.refresh(db_patient)

    return db_patient


def delete_patient(
    db: Session,
    patient_id: int
):
    db_patient = (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )

    if not db_patient:
        return False

    db.delete(db_patient)
    db.commit()

    return True

def search_patients(
    db: Session,
    name: str
):
    return (
        db.query(Patient)
        .filter(Patient.full_name.ilike(f"%{name}%"))
        .all()
    )