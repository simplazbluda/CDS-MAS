from fastapi import FastAPI
from pydantic import BaseModel

from app.services.triage_engine import triage
from app.services.dataset import load_dataset

app = FastAPI(title="Clinical AI Triage System")

dataset = load_dataset()


class PatientInput(BaseModel):
    age: int
    gender: str
    symptoms: str


@app.get("/")
def home():
    return {"status": "AI triage system running"}


@app.post("/triage")
def triage_patient(data: PatientInput):
    result = triage(data.symptoms, dataset)

    return {
        "patient": {
            "age": data.age,
            "gender": data.gender,
            "symptoms": data.symptoms
        },
        "triage_result": result
    }