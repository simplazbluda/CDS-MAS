from backend.app.agents.triage_agent import TriageAgent


agent = TriageAgent()


result = agent.assess(
    "Patient has chest pain, sweating and difficulty breathing"
)


print(result)