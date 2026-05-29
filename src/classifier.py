def classify_ioc(enriched_ioc):

    risk = enriched_ioc["risk"]

    if risk >= 80:
        return "CRITICAL"
    elif risk >= 60:
        return "HIGH"
    elif risk >= 30:
        return "MEDIUM"
    else:
        return "LOW"