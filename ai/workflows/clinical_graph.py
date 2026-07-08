"""
Clinical Multi-Agent Workflow
"""

from typing import TypedDict

from langgraph.graph import StateGraph, END

from backend.app.agents.triage_agent import TriageAgent
from backend.app.agents.knowledge_agent import KnowledgeAgent
from backend.app.agents.documentation_agent import DocumentationAgent



class ClinicalState(TypedDict):

    symptoms: str

    patient_information: str

    triage_result: str

    knowledge_result: str

    clinical_note: str



# Initialize agents

triage_agent = TriageAgent()

knowledge_agent = KnowledgeAgent()

documentation_agent = DocumentationAgent()



def triage_node(state: ClinicalState):

    result = triage_agent.assess(
        state["symptoms"]
    )

    state["triage_result"] = result

    return state



def knowledge_node(state: ClinicalState):

    result = knowledge_agent.analyze(
        state["triage_result"]
    )

    state["knowledge_result"] = result

    return state



def documentation_node(state: ClinicalState):

    note = documentation_agent.generate_note(
        patient_information=state["patient_information"],
        clinical_findings=(
            state["knowledge_result"]
        )
    )

    state["clinical_note"] = note

    return state



def create_clinical_graph():

    workflow = StateGraph(
        ClinicalState
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



clinical_graph = create_clinical_graph()