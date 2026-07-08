from ai.workflows.clinical_graph import clinical_graph


result = clinical_graph.invoke(
    {
        "symptoms":
        """
        Patient has chest pain,
        sweating and difficulty breathing.
        """,

        "patient_information":
        """
        Age:45
        Gender:Male
        """,

        "triage_result":"",
        "knowledge_result":"",
        "clinical_note":""
    }
)


print("====================")
print("TRIAGE RESULT")
print("====================")

print(result["triage_result"])


print("\n====================")
print("CLINICAL NOTE")
print("====================")

print(result["clinical_note"])
print("\nKNOWLEDGE:")
print(result["knowledge_result"])