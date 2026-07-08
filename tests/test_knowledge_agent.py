from backend.app.agents.knowledge_agent import KnowledgeAgent


agent = KnowledgeAgent()


result = agent.analyze(
    """
45 year old male.
Chest pain.
Sweating.
Shortness of breath.
"""
)


print(result)