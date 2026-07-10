from ai.workflows.clinical_graph import clinical_graph


result = clinical_graph.invoke(
    {
        "patient_id": 1,

        "symptoms":
        "Chest pain with shortness of breath",

        "patient_information":
        """
        Patient:
        John Moyo
        Age:
        45
        """
    }
)


print("\nFINAL RESULT\n")

print(result["clinical_note"])