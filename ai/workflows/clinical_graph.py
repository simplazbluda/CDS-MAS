"""
Clinical Multi-Agent Workflow

Pipeline:

Patient Input
        |
Encounter Creation
        |
Patient Context Retrieval
        |
Verified Clinical Facts Construction
        |
Triage Agent
        |
Knowledge Agent
        |
Documentation Agent
        |
Database Persistence
"""


from typing import TypedDict, Optional

from langgraph.graph import StateGraph, END


from backend.app.agents.triage_agent import TriageAgent
from backend.app.agents.knowledge_agent import KnowledgeAgent
from backend.app.agents.documentation_agent import DocumentationAgent


from ai.services.database_service import DatabaseService




# =====================================================
# Workflow State
# =====================================================


class ClinicalState(TypedDict):

    patient_id: int

    encounter_id: int

    symptoms: str

    patient_information: str

    patient_history: str

    clinical_facts: str

    triage_result: Optional[str]

    knowledge_result: Optional[str]

    clinical_note: Optional[str]





# =====================================================
# Initialize Services
# =====================================================


triage_agent = TriageAgent()

knowledge_agent = KnowledgeAgent()

documentation_agent = DocumentationAgent()

database_service = DatabaseService()






# =====================================================
# Encounter Creation Node
# =====================================================


def encounter_node(
    state: ClinicalState
):


    encounter_id = database_service.save_encounter(

        patient_id=
            state["patient_id"],

        symptoms=
            state["symptoms"]

    )


    state["encounter_id"] = encounter_id


    return state






# =====================================================
# Patient Context Retrieval Node
# =====================================================


def patient_context_node(
    state: ClinicalState
):


    patient = database_service.get_patient(

        state["patient_id"]

    )


    history = database_service.get_history(

        state["patient_id"]

    )



    # -----------------------------
    # Patient Information
    # -----------------------------


    if patient:


        patient_information = f"""

Patient Information:

Name:
{patient.first_name} {patient.last_name}


Gender:
{patient.gender}


Date of Birth:
{patient.date_of_birth}


Phone:
{patient.phone}

"""


    else:


        patient_information = """

Patient Information:

Not documented.

"""





    # -----------------------------
    # Patient History
    # -----------------------------


    if history:


        patient_history = history


    else:


        patient_history = (
            "No previous history documented."
        )





    # -----------------------------
    # Verified Clinical Facts
    # -----------------------------


    clinical_facts = f"""

================================

VERIFIED CLINICAL DATA

================================


{patient_information}



CURRENT SYMPTOMS:


{state["symptoms"]}



PREVIOUS HISTORY:


{patient_history}



RULES:

- Use only supplied information.
- Do not infer missing information.
- Do not create undocumented facts.

"""



    state["patient_information"] = patient_information

    state["patient_history"] = patient_history

    state["clinical_facts"] = clinical_facts



    return state







# =====================================================
# Triage Agent Node
# =====================================================


def triage_node(
    state: ClinicalState
):


    result = triage_agent.assess(

        clinical_facts=
            state["clinical_facts"]

    )



    if not result:


        result = (
            "No triage result generated."
        )



    state["triage_result"] = result



    database_service.save_recommendation(

        encounter_id=
            state["encounter_id"],


        agent=
            "TriageAgent",


        recommendation=
            result

    )


    return state






# =====================================================
# Knowledge Agent Node
# =====================================================


def knowledge_node(
    state: ClinicalState
):


    result = knowledge_agent.analyze(

        patient_information=
            state["patient_information"],


        symptoms=
            state["symptoms"],


        patient_history=
            state["patient_history"],


        triage_result=
            state["triage_result"]

    )


    if not result:

        result = (
            "Knowledge assessment not generated."
        )


    state["knowledge_result"] = result



    database_service.save_recommendation(

        encounter_id=
            state["encounter_id"],

        agent=
            "KnowledgeAgent",

        recommendation=
            result

    )


    return state







# =====================================================
# Documentation Agent Node
# =====================================================


def documentation_node(
    state: ClinicalState
):


    note = documentation_agent.generate_note(

        patient_information=
            state["patient_information"],


        symptoms=
            state["symptoms"],


        patient_history=
            state["patient_history"],


        triage_result=
            state["triage_result"],


        clinical_findings=
            state["knowledge_result"]

    )



    if not note:

        note="Clinical note not generated."



    state["clinical_note"]=note



    database_service.save_note(

        encounter_id=
            state["encounter_id"],

        note=
            note

    )


    return state





# =====================================================
# Create LangGraph Workflow
# =====================================================


def create_clinical_graph():


    workflow = StateGraph(

        ClinicalState

    )



    workflow.add_node(

        "encounter",

        encounter_node

    )



    workflow.add_node(

        "patient_context",

        patient_context_node

    )



    workflow.add_node(

        "triage",

        triage_node

    )



    workflow.add_node(

        "knowledge",

        knowledge_node

    )



    workflow.add_node(

        "documentation",

        documentation_node

    )





    workflow.set_entry_point(

        "encounter"

    )



    workflow.add_edge(

        "encounter",

        "patient_context"

    )



    workflow.add_edge(

        "patient_context",

        "triage"

    )



    workflow.add_edge(

        "triage",

        "knowledge"

    )



    workflow.add_edge(

        "knowledge",

        "documentation"

    )



    workflow.add_edge(

        "documentation",

        END

    )



    return workflow.compile()





# =====================================================
# Compiled Graph
# =====================================================


clinical_graph = create_clinical_graph()