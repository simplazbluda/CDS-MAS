"""
Clinical Multi-Agent Workflow

Orchestrates:
- Encounter creation
- Triage Agent
- Knowledge Agent
- Documentation Agent
- Database persistence
"""

from typing import TypedDict

from langgraph.graph import StateGraph, END

from backend.app.agents.triage_agent import TriageAgent
from backend.app.agents.knowledge_agent import KnowledgeAgent
from backend.app.agents.documentation_agent import DocumentationAgent

from ai.services.database_service import DatabaseService



class ClinicalState(TypedDict):

    # Database information
    patient_id: int
    encounter_id: int

    # Clinical input
    symptoms: str
    patient_information: str

    # Agent outputs
    triage_result: str
    knowledge_result: str
    clinical_note: str



# -----------------------------
# Initialize services and agents
# -----------------------------

triage_agent = TriageAgent()

knowledge_agent = KnowledgeAgent()

documentation_agent = DocumentationAgent()

database_service = DatabaseService()



# -----------------------------
# Workflow Nodes
# -----------------------------


def encounter_node(state: ClinicalState):
    """
    Creates a patient encounter
    before AI processing starts.
    """

    encounter_id = database_service.save_encounter(
        patient_id=state["patient_id"],
        symptoms=state["symptoms"]
    )

    state["encounter_id"] = encounter_id

    return state



def triage_node(state: ClinicalState):
    """
    Performs clinical triage.
    """

    result = triage_agent.assess(
        state["symptoms"]
    )

    state["triage_result"] = result


    database_service.save_recommendation(
        encounter_id=state["encounter_id"],
        agent="TriageAgent",
        recommendation=result
    )


    return state



def knowledge_node(state: ClinicalState):
    """
    Retrieves clinical knowledge
    using RAG.
    """

    result = knowledge_agent.analyze(
        state["triage_result"]
    )


    state["knowledge_result"] = result


    database_service.save_recommendation(
        encounter_id=state["encounter_id"],
        agent="KnowledgeAgent",
        recommendation=result
    )


    return state



def documentation_node(state: ClinicalState):
    """
    Generates clinical documentation.
    """

    note = documentation_agent.generate_note(
        patient_information=
            state["patient_information"],

        clinical_findings=
            state["knowledge_result"]
    )


    state["clinical_note"] = note


    database_service.save_note(
        encounter_id=state["encounter_id"],
        note=note
    )


    return state



# -----------------------------
# Create LangGraph Workflow
# -----------------------------


def create_clinical_graph():

    workflow = StateGraph(
        ClinicalState
    )


    workflow.add_node(
        "encounter",
        encounter_node
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



# Compiled workflow

clinical_graph = create_clinical_graph()