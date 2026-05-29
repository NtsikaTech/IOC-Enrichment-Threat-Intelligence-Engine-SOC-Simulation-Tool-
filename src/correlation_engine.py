from collections import defaultdict

def group_iocs_by_risk(results):
    groups = {
        "CRITICAL": [],
        "HIGH": [],
        "MEDIUM": [],
        "LOW": []
    }

    for r in results:
        risk = r["classification"]

        if risk == "CRITICAL":
            groups["CRITICAL"].append(r)
        elif risk == "HIGH":
            groups["HIGH"].append(r)
        elif risk == "MEDIUM":
            groups["MEDIUM"].append(r)
        else:
            groups["LOW"].append(r)

    return groups


def detect_campaigns(results):

    campaigns = []

    malicious = [r for r in results if r["classification"] in ["HIGH", "CRITICAL"]]

    if len(malicious) >= 2:
        campaigns.append({
            "campaign_type": "Multi-IOC Threat Campaign",
            "ioc_count": len(malicious),
            "severity": "HIGH",
            "description": "Multiple high-risk indicators detected across threat intelligence sources"
        })

    return campaigns