from backend.app.database.connection import SessionLocal

from backend.app.database.crud import (
    create_patient,
    create_encounter,
    save_clinical_note
)


db = SessionLocal()


patient = create_patient(
    db,
    "John",
    "Moyo",
    "Male"
)


encounter = create_encounter(
    db,
    patient.id,
    "Chest pain and shortness of breath"
)


note = save_clinical_note(
    db,
    encounter.id,
    """
AI assessment:
Patient requires urgent clinical evaluation.
"""
)


print("Patient:", patient.id)

print("Encounter:", encounter.id)

print("Clinical Note:", note.id)


db.close()