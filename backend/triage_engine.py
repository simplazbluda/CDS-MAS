def rule_based_triage(symptoms: str):
    symptoms = symptoms.lower()

    if "chest pain" in symptoms or "shortness of breath" in symptoms:
        return "urgent", "possible cardiac or respiratory emergency"

    if "stiff neck" in symptoms or "severe headache" in symptoms:
        return "urgent", "possible neurological infection (e.g., meningitis)"

    if "fever" in symptoms and "cough" in symptoms:
        return "non-urgent", "likely respiratory infection"

    return "non-urgent", "general consultation recommended"


def match_dataset(symptoms, dataset):
    symptoms = symptoms.lower()

    for item in dataset:
        if item["symptoms"] in symptoms or symptoms in item["symptoms"]:
            return item

    return None


def triage(symptoms, dataset):
    matched = match_dataset(symptoms, dataset)

    if matched:
        return {
            "source": "dataset_match",
            "label": matched["label"],
            "condition": matched["condition"]
        }

    label, condition = rule_based_triage(symptoms)

    return {
        "source": "rule_based",
        "label": label,
        "condition": condition
    }