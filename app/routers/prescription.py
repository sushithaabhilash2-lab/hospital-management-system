from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.dependencies.roles import require_admin
from app.models.user import User

from app.schemas.prescription import (
    PrescriptionCreate,
    PrescriptionUpdate,
    PrescriptionResponse,
)

from app.services.prescription_service import (
    create_prescription,
    get_all_prescriptions,
    get_prescription_by_id,
    update_prescription,
    delete_prescription,
)

router = APIRouter(
    prefix="/prescriptions",
    tags=["Prescriptions"]
)


@router.post(
    "/",
    response_model=PrescriptionResponse,
    status_code=201
)
def create_new_prescription(
    prescription: PrescriptionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return create_prescription(db, prescription)


@router.get(
    "/",
    response_model=list[PrescriptionResponse]
)
def get_prescriptions(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return get_all_prescriptions(db)


@router.get(
    "/{prescription_id}",
    response_model=PrescriptionResponse
)
def get_prescription(
    prescription_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    prescription = get_prescription_by_id(
        db,
        prescription_id
    )

    if prescription is None:
        raise HTTPException(
            status_code=404,
            detail="Prescription not found"
        )

    return prescription


@router.put(
    "/{prescription_id}",
    response_model=PrescriptionResponse
)
def update_existing_prescription(
    prescription_id: int,
    prescription: PrescriptionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    updated = update_prescription(
        db,
        prescription_id,
        prescription
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Prescription not found"
        )

    return updated


@router.delete(
    "/{prescription_id}"
)
def remove_prescription(
    prescription_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    deleted = delete_prescription(
        db,
        prescription_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Prescription not found"
        )

    return {
        "message": "Prescription deleted successfully."
    }