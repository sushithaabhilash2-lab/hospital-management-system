from pydantic import BaseModel


class PatientCreate(BaseModel):
    full_name: str
    age: int
    gender: str
    phone: str
    address: str


class PatientUpdate(BaseModel):
    full_name: str
    age: int
    gender: str
    phone: str
    address: str


class PatientResponse(BaseModel):
    id: int
    full_name: str
    age: int
    gender: str
    phone: str
    address: str
    user_id: str

    model_config = {
        "from_attributes": True
    }