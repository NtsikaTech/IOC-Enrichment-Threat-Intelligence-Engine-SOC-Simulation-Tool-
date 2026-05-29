import json

def load_iocs():
    with open("data/sample_iocs.json", "r") as f:
        return json.load(f)