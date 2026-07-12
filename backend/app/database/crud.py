from sqlalchemy.orm import Session

from .models import (
    Patient,
    Encounter,
    ClinicalNote,
    AIRecommendation
)



# ==========================
# PATIENT CRUD
# ==========================


def create_patient(
    db: Session,
    first_name: str,
    last_name: str,
    date_of_birth=None,
    gender: str = None,
    phone: str = None
):

    patient = Patient(

        first_name=first_name,

        last_name=last_name,

        date_of_birth=date_of_birth,

        gender=gender,

        phone=phone

    )


    db.add(patient)

    db.commit()

    db.refresh(patient)


    return patient





def get_patients(
    db: Session
):

    return (

        db.query(Patient)

        .all()

    )





def get_patient(
    db: Session,
    patient_id: int
):

    return (

        db.query(Patient)

        .filter(
            Patient.id == patient_id
        )

        .first()

    )





def update_patient(
    db: Session,
    patient_id: int,
    first_name: str,
    last_name: str,
    phone: str = None
):

    patient = get_patient(

        db,

        patient_id

    )


    if patient:


        patient.first_name = first_name

        patient.last_name = last_name

        patient.phone = phone


        db.commit()

        db.refresh(patient)



    return patient





def delete_patient(
    db: Session,
    patient_id: int
):

    patient = get_patient(

        db,

        patient_id

    )


    if patient:


        db.delete(patient)

        db.commit()



    return patient





# ==========================
# PATIENT HISTORY
# ==========================


def get_patient_history(
    db: Session,
    patient_id: int
):
    """
    Retrieves previous patient encounters.

    Returns:
        List[Encounter]

    Formatting is handled by
    DatabaseService.
    """


    encounters = (

        db.query(Encounter)

        .filter(

            Encounter.patient_id == patient_id

        )

        .order_by(

            Encounter.created_at.desc()

        )

        .limit(10)

        .all()

    )


    return encounters





# ==========================
# ENCOUNTER CRUD
# ==========================


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





# ==========================
# CLINICAL NOTE CRUD
# ==========================


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





# ==========================
# AI RECOMMENDATIONS
# ==========================


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