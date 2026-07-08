from sqlalchemy.orm import Session

from app.models.prescription import Prescription
from app.schemas.prescription import (
    PrescriptionCreate,
    PrescriptionUpdate
)


def create_prescription(db: Session, prescription: PrescriptionCreate):
    db_prescription = Prescription(
        medicine=prescription.medicine,
        dosage=prescription.dosage,
        instructions=prescription.instructions,
        appointment_id=prescription.appointment_id
    )

    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)

    return db_prescription


def get_all_prescriptions(db: Session):
    return db.query(Prescription).all()


def get_prescription_by_id(db: Session, prescription_id: int):
    return (
        db.query(Prescription)
        .filter(Prescription.id == prescription_id)
        .first()
    )


def update_prescription(
    db: Session,
    prescription_id: int,
    prescription: PrescriptionUpdate
):
    db_prescription = (
        db.query(Prescription)
        .filter(Prescription.id == prescription_id)
        .first()
    )

    if not db_prescription:
        return None

    db_prescription.medicine = prescription.medicine
    db_prescription.dosage = prescription.dosage
    db_prescription.instructions = prescription.instructions
    db_prescription.appointment_id = prescription.appointment_id

    db.commit()
    db.refresh(db_prescription)

    return db_prescription


def delete_prescription(db: Session, prescription_id: int):
    db_prescription = (
        db.query(Prescription)
        .filter(Prescription.id == prescription_id)
        .first()
    )

    if not db_prescription:
        return False

    db.delete(db_prescription)
    db.commit()

    return True