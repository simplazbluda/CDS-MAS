from backend.app.database.connection import SessionLocal
from backend.app.database.crud import (
    create_encounter,
    get_patient_history
)


def test_create_encounter():

    db = SessionLocal()

    patient_id = 1

    encounter = create_encounter(
        db,
        patient_id,
        "severe headache"
    )


    assert encounter.id is not None

    assert encounter.symptoms == "severe headache"


    db.close()



def test_patient_history():

    db = SessionLocal()


    history = get_patient_history(
        db,
        1
    )


    assert history is not None


    db.close()