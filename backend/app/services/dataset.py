import json
from pathlib import Path


def load_dataset():

    dataset_path = (
        Path(__file__).resolve()
        .parent.parent
        / "data"
        / "synthetic_patients.json"
    )

    with open(dataset_path, "r") as f:
        return json.load(f)