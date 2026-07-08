from pydantic import BaseModel


class AppointmentCreate(BaseModel):
    appointment_date: str
    appointment_time: str
    reason: str
    patient_id: int
    doctor_id: int


class AppointmentUpdate(BaseModel):
    appointment_date: str
    appointment_time: str
    reason: str
    patient_id: int
    doctor_id: int


class AppointmentResponse(BaseModel):
    id: int
    appointment_date: str
    appointment_time: str
    reason: str
    patient_id: int
    doctor_id: int

    model_config = {
        "from_attributes": True
    }