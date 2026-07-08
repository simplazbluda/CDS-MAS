from ai.services.knowledge_service import KnowledgeService
from ai.models.phi3 import Phi3Model


class KnowledgeAgent:
    """
    Agent responsible for retrieving medical knowledge
    and generating evidence-supported clinical guidance.
    """


    def __init__(self):

        self.knowledge_service = KnowledgeService()
        self.model = Phi3Model()



    def analyze(self, clinical_case: str):

        # Retrieve relevant medical information

        documents = self.knowledge_service.retrieve_information(
            clinical_case
        )


        context = "\n".join(
            documents[0]
        )


        prompt = f"""
You are a clinical knowledge assistant.

Use the following medical information:

{context}


Analyze this clinical case:

{clinical_case}


Provide:

1. Relevant clinical considerations
2. Possible risks
3. Recommended next steps

Do not provide a final diagnosis.
Support clinician decision making.
"""


        response = self.model.generate(
            prompt
        )


        return response