from fastapi import APIRouter
from datetime import date

from pydantic import BaseModel

from backend.app.database.connection import SessionLocal

from backend.app.database.crud import (
    create_patient,
    get_patients,
    get_patient,
    update_patient,
    delete_patient
)


router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)



# ==========================
# Request Models
# ==========================


class PatientCreate(BaseModel):

    first_name: str

    last_name: str

    date_of_birth: date | None = None

    gender: str | None = None

    phone: str | None = None



class PatientUpdate(BaseModel):

    first_name: str

    last_name: str

    phone: str | None = None



# ==========================
# Create Patient
# ==========================


@router.post("/")
def create_new_patient(
    patient: PatientCreate
):

    db = SessionLocal()

    result = create_patient(
        db=db,
        first_name=patient.first_name,
        last_name=patient.last_name,
        date_of_birth=patient.date_of_birth,
        gender=patient.gender,
        phone=patient.phone
    )

    db.close()

    return result



# ==========================
# Get All Patients
# ==========================


@router.get("/")
def read_patients():

    db = SessionLocal()

    patients = get_patients(db)

    db.close()

    return patients



# ==========================
# Get Single Patient
# ==========================


@router.get("/{patient_id}")
def read_patient(
    patient_id: int
):

    db = SessionLocal()

    patient = get_patient(
        db,
        patient_id
    )

    db.close()

    return patient



# ==========================
# Update Patient
# ==========================


@router.put("/{patient_id}")
def edit_patient(
    patient_id: int,
    patient: PatientUpdate
):

    db = SessionLocal()

    result = update_patient(
        db=db,
        patient_id=patient_id,
        first_name=patient.first_name,
        last_name=patient.last_name,
        phone=patient.phone
    )

    db.close()

    return result



# ==========================
# Delete Patient
# ==========================


@router.delete("/{patient_id}")
def remove_patient(
    patient_id: int
):

    db = SessionLocal()

    delete_patient(
        db,
        patient_id
    )

    db.close()

    return {
        "message":
        "Patient deleted successfully"
    }