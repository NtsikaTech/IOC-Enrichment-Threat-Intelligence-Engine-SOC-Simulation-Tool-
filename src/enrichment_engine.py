from src.threat_db import THREAT_DB
from src.mitre_mapper import map_to_mitre

def enrich_ioc(ioc):

    ioc_type = ioc["type"]
    value = ioc["value"]

    data = THREAT_DB.get(ioc_type, {}).get(value)

    mitre = map_to_mitre(ioc_type, data if data else {})

    if data:
        return {
            "type": ioc_type,
            "value": value,
            "risk": data["risk"],
            "category": data["category"],
            "tag": data["tag"],
            "mitre_technique": mitre["technique"],
            "mitre_tactic": mitre["tactic"],
            "status": "KNOWN THREAT"
        }

    return {
        "type": ioc_type,
        "value": value,
        "risk": 20,
        "category": "Unknown",
        "tag": "No intelligence found",
        "mitre_technique": mitre["technique"],
        "mitre_tactic": mitre["tactic"],
        "status": "UNKNOWN"
    }