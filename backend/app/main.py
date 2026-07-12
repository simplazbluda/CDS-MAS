from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api import (
    health,
    clinical,
    patients,
    encounters
)


app = FastAPI(
    title="MedicalAI Clinical Decision Support System",
    version="0.1"
)

# ==============================
# CORS
# ==============================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=[
        "*"
    ],
    allow_headers=[
        "*"
    ],
)

app.include_router(
    health.router
)

app.include_router(
    clinical.router
)

app.include_router(
    patients.router
)

app.include_router(
    encounters.router
)


@app.get("/")
def root():

    return {
        "message":
        "MedicalAI API running"
    }