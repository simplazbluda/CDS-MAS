from ai.workflows.clinical_graph import clinical_graph



def test_ai_workflow_execution():


    result = clinical_graph.invoke(

        {

            "patient_id":1,

            "encounter_id":0,

            "symptoms":
            "persistent chest pain",

            "patient_information":"",

            "patient_history":"",

            "clinical_facts":"",

            "triage_result":None,

            "knowledge_result":None,

            "clinical_note":None

        }

    )


    assert result is not None


    assert result["triage_result"] is not None


    assert result["clinical_note"] is not None