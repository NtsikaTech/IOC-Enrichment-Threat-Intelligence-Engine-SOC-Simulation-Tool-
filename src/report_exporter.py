import json
import os
from datetime import datetime

def export_report(results, groups, campaigns):

    os.makedirs("reports", exist_ok=True)

    report = {
        "metadata": {
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tool": "IOC Enrichment & Threat Intelligence Engine",
            "version": "2.0"
        },
        "summary": {
            "total_iocs": len(results),
            "critical": len(groups["CRITICAL"]),
            "high": len(groups["HIGH"]),
            "medium": len(groups["MEDIUM"]),
            "low": len(groups["LOW"])
        },
        "ioc_results": results,
        "campaigns_detected": campaigns
    }

    file_path = "reports/soc_threat_report.json"

    with open(file_path, "w") as f:
        json.dump(report, f, indent=4)

    return file_path