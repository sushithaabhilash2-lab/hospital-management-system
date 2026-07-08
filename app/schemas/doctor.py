from pydantic import BaseModel


class DoctorCreate(BaseModel):
    full_name: str
    specialization: str
    experience: int
    phone: str


class DoctorUpdate(BaseModel):
    full_name: str
    specialization: str
    experience: int
    phone: str


class DoctorResponse(BaseModel):
    id: int
    full_name: str
    specialization: str
    experience: int
    phone: str
    user_id: str

    model_config = {
        "from_attributes": True
    }