from backend.app.database.connection import SessionLocal

from backend.app.database.crud import (
    create_encounter,
    save_clinical_note,
    save_ai_recommendation
)



class DatabaseService:
    """
    Handles communication between
    AI agents and the database.
    """


    def save_encounter(
        self,
        patient_id: int,
        symptoms: str
    ):

        db = SessionLocal()

        try:
            encounter = create_encounter(
                db,
                patient_id,
                symptoms
            )

            return encounter.id

        finally:
            db.close()



    def save_note(
        self,
        encounter_id: int,
        note: str
    ):

        db = SessionLocal()

        try:

            result = save_clinical_note(
                db,
                encounter_id,
                note
            )

            return result.id

        finally:
            db.close()



    def save_recommendation(
        self,
        encounter_id: int,
        agent: str,
        recommendation: str
    ):

        db = SessionLocal()

        try:

            result = save_ai_recommendation(
                db,
                encounter_id,
                agent,
                recommendation
            )

            return result.id

        finally:
            db.close()