from fastapi import Depends, HTTPException

from app.dependencies.auth import get_current_user
from app.models.user import User, UserRole


def require_admin(
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user


def require_doctor(
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.DOCTOR:
        raise HTTPException(
            status_code=403,
            detail="Doctor access required"
        )

    return current_user


def require_patient(
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.PATIENT:
        raise HTTPException(
            status_code=403,
            detail="Patient access required"
        )

    return current_user