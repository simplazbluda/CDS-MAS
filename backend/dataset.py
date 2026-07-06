import json

def load_dataset():
    with open("backend/data/synthetic_patients.json", "r") as f:
        return json.load(f)