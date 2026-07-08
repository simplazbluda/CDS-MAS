from ai.rag.vector_store import MedicalKnowledgeBase


kb = MedicalKnowledgeBase()


kb.add_document(
    "emergency1",
    """
    Chest pain with shortness of breath
    requires urgent medical assessment.
    """
)


results = kb.search(
    "patient has chest pain"
)


print(results)