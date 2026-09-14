def calculate_priority(severity):
    severity = severity.lower()

    if severity == "high":
        return "High"
    elif severity == "medium":
        return "Medium"
    else:
        return "Low"
