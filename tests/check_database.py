from backend.app.database.connection import SessionLocal
from backend.app.database.models import (
    Patient,
    Encounter,
    ClinicalNote,
    AIRecommendation
)


db = SessionLocal()


print("\n=== PATIENTS ===")

patients = db.query(Patient).all()

for patient in patients:
    print(
        patient.id,
        patient.first_name,
        patient.last_name,
        patient.gender
    )


print("\n=== ENCOUNTERS ===")

encounters = db.query(Encounter).all()

for encounter in encounters:
    print(
        "ID:",
        encounter.id,
        "Patient:",
        encounter.patient_id,
        "Symptoms:",
        encounter.symptoms
    )


print("\n=== CLINICAL NOTES ===")

notes = db.query(ClinicalNote).all()

for note in notes:
    print(
        "ID:",
        note.id,
        "Encounter:",
        note.encounter_id
    )

    print(
        note.ai_generated_note
    )


print("\n=== AI RECOMMENDATIONS ===")

recommendations = db.query(
    AIRecommendation
).all()


for rec in recommendations:

    print(
        "Agent:",
        rec.agent_name
    )

    print(
        rec.recommendation
    )


db.close()