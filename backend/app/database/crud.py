from sqlalchemy.orm import Session

from .models import (
    Patient,
    Encounter,
    ClinicalNote,
    AIRecommendation
)



def create_patient(
    db: Session,
    first_name: str,
    last_name: str,
    gender: str = None
):

    patient = Patient(
        first_name=first_name,
        last_name=last_name,
        gender=gender
    )

    db.add(patient)
    db.commit()
    db.refresh(patient)

    return patient



def create_encounter(
    db: Session,
    patient_id: int,
    symptoms: str
):

    encounter = Encounter(
        patient_id=patient_id,
        symptoms=symptoms
    )

    db.add(encounter)
    db.commit()
    db.refresh(encounter)

    return encounter



def save_clinical_note(
    db: Session,
    encounter_id: int,
    ai_note: str
):

    note = ClinicalNote(
        encounter_id=encounter_id,
        ai_generated_note=ai_note
    )

    db.add(note)
    db.commit()
    db.refresh(note)

    return note



def save_ai_recommendation(
    db: Session,
    encounter_id: int,
    agent_name: str,
    recommendation: str
):

    result = AIRecommendation(
        encounter_id=encounter_id,
        agent_name=agent_name,
        recommendation=recommendation
    )

    db.add(result)
    db.commit()
    db.refresh(result)

    return result