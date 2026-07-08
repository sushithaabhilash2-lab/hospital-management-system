from pydantic import BaseModel


class PrescriptionCreate(BaseModel):
    medicine: str
    dosage: str
    instructions: str
    appointment_id: int


class PrescriptionUpdate(BaseModel):
    medicine: str
    dosage: str
    instructions: str
    appointment_id: int


class PrescriptionResponse(BaseModel):
    id: int
    medicine: str
    dosage: str
    instructions: str
    appointment_id: int

    model_config = {
        "from_attributes": True
    }