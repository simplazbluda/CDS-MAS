from fastapi import APIRouter


router = APIRouter()


@router.get("/health")
def health_check():

    return {
        "status": "healthy",
        "system": "MedicalAI CDS-MAS"
    }