def estimate_cost(damage_type, severity):
    damage_type = damage_type.lower()
    severity = severity.lower()

    if damage_type == "pothole":
        if severity == "high":
            return 5000
        elif severity == "medium":
            return 3000
        else:
            return 1500

    elif damage_type == "crack":
        if severity == "high":
            return 4000
        elif severity == "medium":
            return 2500
        else:
            return 1000

    return 2000
