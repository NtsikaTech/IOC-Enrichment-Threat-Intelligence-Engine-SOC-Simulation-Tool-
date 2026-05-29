from src.ioc_input import load_iocs
from src.enrichment_engine import enrich_ioc
from src.classifier import classify_ioc
from src.risk_engine import calculate_ioc_risk
from src.report_exporter import export_report
from src.correlation_engine import group_iocs_by_risk, detect_campaigns
from src.report_exporter import export_report

def run():

    iocs = load_iocs()
    results = []

    print("\n===== IOC ENRICHMENT REPORT =====\n")

    # =========================
    # STEP 1: PROCESS IOCs
    # =========================
    for ioc in iocs:

        enriched = enrich_ioc(ioc)

        classification = classify_ioc(enriched)

        final_risk = calculate_ioc_risk(enriched)

        enriched["classification"] = classification
        enriched["final_risk"] = final_risk

        results.append(enriched)

        # SOC-style output
        print(f"IOC: {ioc['value']}")
        print(f"Status: {enriched['status']}")
        print(f"Base Risk: {enriched['risk']}")
        print(f"Final Risk: {final_risk}")
        print(f"Classification: {classification}")
        print(f"MITRE Technique: {enriched.get('mitre_technique', 'N/A')}")
        print(f"MITRE Tactic: {enriched.get('mitre_tactic', 'N/A')}")
        print("-" * 50)

    # =========================
    # STEP 2: CORRELATION ENGINE
    # =========================
    groups = group_iocs_by_risk(results)
    campaigns = detect_campaigns(results)

    print("\n===== SOC CORRELATION REPORT =====\n")

    for level, items in groups.items():
        print(f"{level}: {len(items)} IOCs")

    print("\n===== CAMPAIGN DETECTION =====\n")

    if campaigns:
        for c in campaigns:
            print(f"🚨 {c['campaign_type']}")
            print(f"IOC Count: {c['ioc_count']}")
            print(f"Severity: {c['severity']}")
            print(f"Description: {c['description']}")
            print("-" * 50)
    else:
        print("No coordinated campaigns detected")

    # =========================
    # STEP 3: EXPORT REPORT
    # =========================
    file_path = export_report(results, groups, campaigns)

    print("\n===== SOC REPORT GENERATED =====")
    print(f"Report saved to: {file_path}")


if __name__ == "__main__":
    run()