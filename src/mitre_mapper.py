def map_to_mitre(ioc_type, enriched_data):

    mapping = {
        "ip": {
            "tag": "Tor Exit Node",
            "technique": "T1090",
            "tactic": "Command and Control"
        },
        "domain": {
            "tag": "Credential Harvesting",
            "technique": "T1566",
            "tactic": "Phishing"
        },
        "hash": {
            "tag": "Common Malware Signature",
            "technique": "T1003",
            "tactic": "Credential Access"
        }
    }

    default = {
        "technique": "T0000",
        "tactic": "Unknown"
    }

    return mapping.get(ioc_type, default)