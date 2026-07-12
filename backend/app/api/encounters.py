from fastapi import APIRouter
from pydantic import BaseModel

from ai.workflows.clinical_graph import clinical_graph
from ai.services.database_service import DatabaseService



router = APIRouter(
    prefix="/clinical",
    tags=["Clinical Workflow"]
)



database_service = DatabaseService()



class ClinicalRequest(BaseModel):

    patient_id: int

    symptoms: str





@router.post("/workflow")
def run_clinical_workflow(
    request: ClinicalRequest
):


    # -----------------------------
    # Initial workflow state
    # -----------------------------

    state = {

        "patient_id":
            request.patient_id,


        "encounter_id":
            0,


        "symptoms":
            request.symptoms,


        "patient_information":
            None,


        "patient_history":
            None,


        "triage_result":
            None,


        "knowledge_result":
            None,


        "clinical_note":
            None

    }



    # -----------------------------
    # Run LangGraph workflow
    # -----------------------------

    result = clinical_graph.invoke(
        state
    )



    # -----------------------------
    # Retrieve patient information
    # -----------------------------

    patient = database_service.get_patient(

        patient_id=request.patient_id

    )



    patient_data = {

        "id":
            patient.id
            if patient
            else None,


        "name":
            (
                f"{patient.first_name} {patient.last_name}"
                if patient
                else "Not documented."
            ),


        "gender":
            patient.gender
            if patient
            else "Not documented.",


        "date_of_birth":
            str(patient.date_of_birth)
            if patient
            else "Not documented.",


        "phone":
            patient.phone
            if patient
            else "Not documented."

    }




    return {


        "patient":

            patient_data,



        "encounter":

        {

            "id":
                result["encounter_id"],


            "symptoms":
                result["symptoms"]

        },



        "triage":

        {

            "agent":
                "TriageAgent",


            "assessment":
                result["triage_result"]

        },



        "knowledge":

        {

            "agent":
                "KnowledgeAgent",


            "assessment":
                result["knowledge_result"]

        },



        "clinical_note":

            result["clinical_note"]

    }