"""
Medical Knowledge Service

Responsible for:

- Managing medical documents
- Storing embeddings
- Retrieving relevant medical knowledge
- Providing controlled context to KnowledgeAgent
"""


from typing import List


from ai.rag.vector_store import MedicalKnowledgeBase





class KnowledgeService:


    """
    Service layer for medical knowledge retrieval.

    This service ONLY handles
    medical reference information.

    It must never contain:
    - patient data
    - encounters
    - clinical notes
    """



    def __init__(self):

        self.knowledge_base = MedicalKnowledgeBase()





    def add_medical_document(
        self,
        document_id: str,
        content: str
    ):


        """
        Store a medical document.

        Args:

            document_id:
                Unique document identifier.

            content:
                Medical reference content.

        """


        self.knowledge_base.add_document(

            document_id,

            content

        )






    def retrieve_information(
        self,
        query: str,
        top_k: int = 3
    ) -> List[str]:


        """
        Retrieve relevant medical references.


        Args:

            query:
                Clinical knowledge query.


            top_k:
                Number of documents to retrieve.


        Returns:

            List of relevant medical documents.

        """



        if not query:


            return [

                "No clinical query provided."

            ]




        results = self.knowledge_base.search(

            query

        )



        if not results:


            return [

                "No relevant medical references found."

            ]




        # Limit retrieved context

        return results[:top_k]