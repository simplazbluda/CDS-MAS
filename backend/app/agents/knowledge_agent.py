from ai.services.knowledge_service import KnowledgeService
from ai.models.phi3 import Phi3Model




class KnowledgeAgent:

    """
    Provides evidence-supported clinical guidance.

    This agent does NOT diagnose patients.

    It only:
    - retrieves medical knowledge
    - explains clinical considerations
    - identifies risks
    - suggests evaluation steps
    """



    def __init__(self):

        self.service = KnowledgeService()

        self.model = Phi3Model()





    def analyze(
        self,
        patient_information: str,
        symptoms: str,
        patient_history: str,
        triage_result: str
    ):



        # --------------------------------
        # Retrieve medical knowledge
        # --------------------------------


        search_query = f"""

Symptoms:

{symptoms}


Clinical concern:

{triage_result}

"""


        documents = self.service.retrieve_information(

             query=search_query,
             top_k=3

        )



        if documents:


            context = "\n".join(

                documents

            )


        else:


            context = (

                "No medical reference retrieved."

            )





        # --------------------------------
        # Prompt
        # --------------------------------


        prompt = f"""


You are a clinical knowledge support assistant.


Your role:

Provide evidence-based clinical considerations
to support healthcare professionals.


IMPORTANT RULES:


You must NOT:

- diagnose the patient
- create patient facts
- assume missing information
- invent vital signs
- invent examination findings
- invent laboratory results
- invent medications
- invent treatment already given



Patient information:

{patient_information}



Current symptoms:

{symptoms}



Previous history:

{patient_history}



Triage assessment:

{triage_result}



Medical reference information:

{context}




Provide:



1. Clinical Considerations

Discuss possible clinical concerns
based only on the supplied symptoms.



2. Potential Risks

Explain why the situation may require
attention.



3. Recommended Evaluation

Suggest assessments or investigations
that clinicians commonly consider.



4. Knowledge Limitations

Clearly state what information is missing.



Remember:

This is clinical decision support.

It is NOT a diagnosis.

Do not create a patient note.

"""



        return self.model.generate(prompt)