from fastapi import FastAPI
from fastapi import HTTPException
from app.core.exceptions import (
    http_exception_handler,
    general_exception_handler
) 
from app.db.database import Base, engine
from app.models.user import User
from app.models.patient import Patient
from app.models.doctor import Doctor
from app.models.appointment import Appointment
from app.models.prescription import Prescription

from app.routers import user as user_router
from app.routers import auth as auth_router
from app.routers import patient as patient_router
from app.routers import doctor as doctor_router
from app.routers import appointment as appointment_router
from app.routers import prescription as prescription_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hospital Management System"
)

app.include_router(user_router.router)
app.include_router(auth_router.router)
app.include_router(patient_router.router)
app.include_router(doctor_router.router)
app.include_router(appointment_router.router)
app.include_router(prescription_router.router)

@app.get("/")
def home():
    return {
        "message": "Hospital Management System API"
    }

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    Exception,
    general_exception_handler
)