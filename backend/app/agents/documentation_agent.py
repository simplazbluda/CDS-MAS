from ai.models.phi3 import Phi3Model


class DocumentationAgent:
    """
    AI agent responsible for generating
    draft clinical documentation.
    """

    def __init__(self):
        self.model = Phi3Model()


    def generate_note(
        self,
        patient_information: str,
        clinical_findings: str
    ) -> str:
        """
        Generate a draft clinical note.

        Args:
            patient_information:
                Patient demographics and complaint.

            clinical_findings:
                Assessment information.

        Returns:
            Draft clinical note.
        """

        prompt = f"""
You are a clinical documentation assistant.

Create a structured draft clinical note.

Patient information:
{patient_information}

Clinical findings:
{clinical_findings}


Use this structure:

1. Chief Complaint

2. History of Present Illness

3. Relevant Findings

4. Assessment

5. Plan


Important:
- This is a draft only.
- A doctor must review and edit before approval.
- Do not invent patient information.
"""

        return self.model.generate(prompt)