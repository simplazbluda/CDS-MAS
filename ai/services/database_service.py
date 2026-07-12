from backend.app.database.connection import SessionLocal

from backend.app.database.crud import (
    create_encounter,
    save_clinical_note,
    save_ai_recommendation,
    get_patient_history,
    get_patient
)



class DatabaseService:
    """
    Handles communication between:

    Database
        |
        v
    Clinical AI Workflow


    Responsible for:

    - Creating encounters
    - Retrieving patient information
    - Retrieving verified patient history
    - Saving clinical notes
    - Saving AI recommendations

    IMPORTANT:

    AI-generated outputs are stored for audit purposes,
    but they are NOT returned as patient history.
    """



    # =====================================================
    # Create Encounter
    # =====================================================

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



    # =====================================================
    # Save Clinical Note
    # =====================================================

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



    # =====================================================
    # Save AI Recommendation
    # =====================================================

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



    # =====================================================
    # Retrieve Verified Patient History
    # =====================================================

    def get_history(
        self,
        patient_id: int
    ) -> str:

        """
        Returns ONLY verified clinical information.

        Included:
        - Previous encounter dates
        - Reported symptoms
        - Chief complaint (if available)

        Excluded:
        - AI recommendations
        - AI-generated clinical notes

        This prevents AI hallucination feedback loops.
        """

        db = SessionLocal()

        try:

            encounters = get_patient_history(
                db,
                patient_id
            )


            if not encounters:

                return (
                    "No previous clinical history documented."
                )



            formatted_history = ""



            for index, encounter in enumerate(
                encounters,
                start=1
            ):


                formatted_history += f"""

---------------------------------

Previous Encounter {index}


Encounter Date:

{encounter.created_at if encounter.created_at else "Not documented."}



Symptoms:

{encounter.symptoms if encounter.symptoms else "Not documented."}



Chief Complaint:

{encounter.chief_complaint if encounter.chief_complaint else "Not documented."}



"""



            return formatted_history



        finally:

            db.close()



    # =====================================================
    # Retrieve Patient Information
    # =====================================================

    def get_patient(
        self,
        patient_id: int
    ):

        db = SessionLocal()

        try:

            patient = get_patient(
                db,
                patient_id
            )

            return patient


        finally:

            db.close()