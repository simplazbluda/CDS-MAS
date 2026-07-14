from fastapi.testclient import TestClient

from backend.app.main import app



client = TestClient(app)



def test_clinical_workflow():


    response = client.post(

        "/clinical/workflow",

        json={

            "patient_id":1,

            "symptoms":
            "chest pain and dizziness"

        }

    )


    assert response.status_code == 200


    data = response.json()


    assert "triage_result" in data


    assert "clinical_note" in data