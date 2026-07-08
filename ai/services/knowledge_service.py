"""
Medical Knowledge Service

Responsible for managing medical documents,
embeddings, and retrieval from the vector database.
"""


from ai.rag.vector_store import MedicalKnowledgeBase


class KnowledgeService:
    """
    Provides access to the medical knowledge base.
    """


    def __init__(self):

        self.knowledge_base = MedicalKnowledgeBase()



    def add_medical_document(
        self,
        document_id: str,
        content: str
    ):
        """
        Store a medical document in the knowledge base.

        Args:
            document_id:
                Unique identifier for the document.

            content:
                Medical text content.
        """

        self.knowledge_base.add_document(
            document_id,
            content
        )



    def retrieve_information(
        self,
        query: str
    ):
        """
        Retrieve relevant medical information.

        Args:
            query:
                Clinical question or symptom description.

        Returns:
            Relevant medical documents.
        """

        results = self.knowledge_base.search(
            query
        )

        return results