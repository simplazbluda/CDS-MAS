from ai.models.phi3 import Phi3Model


model = Phi3Model()

response = model.generate(
    """
    You are a clinical AI assistant.

    Explain the importance of clinical documentation.
    """
)

print(response)