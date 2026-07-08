from ai.models.phi3 import Phi3Model


class TriageAgent:
    """
    AI agent responsible for initial patient triage.
    """

    def __init__(self):
        self.model = Phi3Model()


    def assess(self, symptoms: str) -> str:
        """
        Analyse patient symptoms and classify urgency.

        Args:
            symptoms: Patient reported symptoms.

        Returns:
            AI generated triage assessment.
        """

        prompt = f"""
You are a clinical triage assistant.

Analyze the following patient symptoms:

{symptoms}

Provide:

1. Urgency level:
   - Emergency
   - Urgent
   - Non-urgent

2. Possible concerns

3. Recommended next steps

Do not provide a final diagnosis.
Support clinical decision making only.
"""

        return self.model.generate(prompt)