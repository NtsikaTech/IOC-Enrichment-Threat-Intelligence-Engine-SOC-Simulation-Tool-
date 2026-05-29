def calculate_ioc_risk(enriched_ioc):

    base = enriched_ioc["risk"]

    if enriched_ioc["type"] == "ip":
        base += 5
    elif enriched_ioc["type"] == "domain":
        base += 10
    elif enriched_ioc["type"] == "hash":
        base += 15

    return min(base, 100)