from ai.services.database_service import DatabaseService


service = DatabaseService()


encounter_id = service.save_encounter(
    patient_id=1,
    symptoms="Fever and cough"
)


print(
    "Created encounter:",
    encounter_id
)


note_id = service.save_note(
    encounter_id,
    "AI recommends further assessment."
)


print(
    "Saved note:",
    note_id
)