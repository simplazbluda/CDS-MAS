from backend.app.agents.documentation_agent import DocumentationAgent


agent = DocumentationAgent()


note = agent.generate_note(
    patient_information="""
Age: 45
Gender: Male
Complaint: Chest pain
""",

    clinical_findings="""
Patient reports chest pain for 2 hours.
Associated sweating and shortness of breath.
"""
)


print(note)