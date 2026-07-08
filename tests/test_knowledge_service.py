from ai.services.knowledge_service import KnowledgeService


service = KnowledgeService()


service.add_medical_document(
    "cardiac001",
    """
    Patients presenting with chest pain,
    sweating and shortness of breath require
    urgent clinical assessment.
    """
)


results = service.retrieve_information(
    "patient has chest pain"
)


print(results)