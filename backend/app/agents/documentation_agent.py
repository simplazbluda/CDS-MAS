from ai.models.phi3 import Phi3Model



class DocumentationAgent:


    def __init__(self):

        self.model = Phi3Model()



    def generate_note(
        self,
        patient_information: str,
        symptoms: str,
        patient_history: str,
        triage_result: str,
        clinical_findings: str
    ):


        prompt=f"""

You are a clinical documentation assistant.

Generate a clinical note ONLY from verified information.

STRICT RULES:

- Never invent patient details.
- Never assume age.
- Never assume diagnosis.
- Never copy facts from AI recommendations.
- Never create medications.
- Never create examinations.
- Never create laboratory results.

If information is missing write:

"Not documented."


====================
PATIENT INFORMATION
====================

{patient_information}



====================
CURRENT SYMPTOMS
====================

{symptoms}



====================
PREVIOUS HISTORY
====================

{patient_history}



====================
TRIAGE OUTPUT
====================

{triage_result}



====================
KNOWLEDGE SUPPORT
====================

{clinical_findings}



Generate:


PATIENT INFORMATION

CHIEF COMPLAINT

HISTORY OF PRESENT ILLNESS

RELEVANT HISTORY

CLINICAL ASSESSMENT

RECOMMENDED NEXT STEPS


IMPORTANT:

This is AI clinical decision support.

The patient has not been physically examined.

Do not create missing information.

"""


        return self.model.generate(prompt)