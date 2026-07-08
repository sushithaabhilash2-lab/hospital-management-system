from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.patient import (
    PatientCreate,
    PatientUpdate,
    PatientResponse,
)
from app.services.patient_service import (
    create_patient,
    get_all_patients,
    get_patient_by_id,
    update_patient,
    delete_patient,
    search_patients
)
from app.dependencies.roles import require_admin

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post(
    "/",
    response_model=PatientResponse,
    status_code=201
)
def create_new_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_patient = create_patient(
        db,
        patient,
        current_user.id
    )

    if new_patient is None:
        raise HTTPException(
            status_code=400,
            detail="Patient profile already exists."
        )

    return new_patient


@router.get(
    "/",
    response_model=list[PatientResponse]
)
def get_patients(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return get_all_patients(
        db,
        skip,
        limit
    )

@router.get(
    "/search",
    response_model=list[PatientResponse]
)
def search_patient(
    name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return search_patients(
        db,
        name
    ) 

@router.get(
    "/{patient_id}",
    response_model=PatientResponse
)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    patient = get_patient_by_id(
        db,
        patient_id
    )

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient

@router.put(
    "/{patient_id}",
    response_model=PatientResponse
)
def update_existing_patient(
    patient_id: int,
    patient: PatientUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    updated_patient = update_patient(
        db,
        patient_id,
        patient
    )

    if updated_patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return updated_patient

@router.delete(
    "/{patient_id}"
)
def remove_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    deleted = delete_patient(
        db,
        patient_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return {
        "message": "Patient deleted successfully."
    }