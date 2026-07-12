from fastapi import APIRouter
from pydantic import BaseModel

from ai.workflows.clinical_graph import clinical_graph


router = APIRouter(
    prefix="/clinical",
    tags=["Clinical Workflow"]
)



# =====================================================
# Request Model
# =====================================================

class ClinicalRequest(BaseModel):

    patient_id: int

    symptoms: str





# =====================================================
# Run Clinical Workflow
# =====================================================

@router.post("/workflow")
def run_clinical_workflow(
    request: ClinicalRequest
):


    result = clinical_graph.invoke(

        {

            # Database

            "patient_id":
                request.patient_id,


            "encounter_id":
                0,



            # Current encounter

            "symptoms":
                request.symptoms,



            # Patient context
            # Filled by patient_context_node

            "patient_information":
                "",


            "patient_history":
                "",



            # Combined facts

            "clinical_facts":
                "",



            # AI outputs

            "triage_result":
                None,


            "knowledge_result":
                None,


            "clinical_note":
                None

        }

    )




    return {


        # ----------------------------
        # Encounter
        # ----------------------------

        "encounter_id":

            result.get(
                "encounter_id"
            ),



        # ----------------------------
        # Patient Context
        # ----------------------------

        "patient_information":

            result.get(
                "patient_information",
                "Not documented."
            ),



        "patient_history":

            result.get(
                "patient_history",
                "Not documented."
            ),




        # ----------------------------
        # Clinical Facts
        # ----------------------------

        "clinical_facts":

            result.get(
                "clinical_facts",
                "Not documented."
            ),




        # ----------------------------
        # Current Symptoms
        # ----------------------------

        "symptoms":

            result.get(
                "symptoms",
                "Not documented."
            ),




        # ----------------------------
        # AI Outputs
        # ----------------------------

        "triage_result":

            result.get(
                "triage_result",
                "Not generated."
            ),



        "knowledge_result":

            result.get(
                "knowledge_result",
                "Not generated."
            ),



        "clinical_note":

            result.get(
                "clinical_note",
                "Not generated."
            )

    }