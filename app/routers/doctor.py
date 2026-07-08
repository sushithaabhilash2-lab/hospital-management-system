from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_admin
from app.models.user import User

from app.schemas.doctor import (
    DoctorCreate,
    DoctorUpdate,
    DoctorResponse
)

from app.services.doctor_service import (
    create_doctor,
    get_all_doctors,
    get_doctor_by_id,
    update_doctor,
    delete_doctor
)

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


@router.post(
    "/",
    response_model=DoctorResponse,
    status_code=201
)
def create_new_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    new_doctor = create_doctor(
        db,
        doctor,
        current_user.id
    )

    if new_doctor is None:
        raise HTTPException(
            status_code=400,
            detail="Doctor profile already exists."
        )

    return new_doctor


@router.get(
    "/",
    response_model=list[DoctorResponse]
)
def get_doctors(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return get_all_doctors(db)


@router.get(
    "/{doctor_id}",
    response_model=DoctorResponse
)
def get_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    doctor = get_doctor_by_id(
        db,
        doctor_id
    )

    if doctor is None:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    return doctor


@router.put(
    "/{doctor_id}",
    response_model=DoctorResponse
)
def update_existing_doctor(
    doctor_id: int,
    doctor: DoctorUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    updated = update_doctor(
        db,
        doctor_id,
        doctor
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    return updated


@router.delete(
    "/{doctor_id}"
)
def remove_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    deleted = delete_doctor(
        db,
        doctor_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    return {
        "message": "Doctor deleted successfully."
    }