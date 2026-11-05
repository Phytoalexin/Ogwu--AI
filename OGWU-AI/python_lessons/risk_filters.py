def calculate_risk_penalty(risks):

    penalty = 0

    if "Friendly" in risks:
        penalty += 10

    if "Key Player Missing" in risks:
        penalty += 10

    if "Heavy Rotation" in risks:
        penalty += 10

    if "Conflicting Evidence" in risks:
        penalty += 15

    if "Small Sample" in risks:
        penalty += 10

    return penalty

risks = [
    "Friendly",
    "Heavy Rotation"
]

penalty = calculate_risk_penalty(risks)

print("Risk Penalty:", penalty)


def apply_risk_penalty(score, penalty):

    final_score = score - penalty

    if final_score < 40:
        final_score = 40

    return final_score

score = 90

final_score = apply_risk_penalty(score, penalty)

print("Original Score:", score)
print("Risk Penalty:", penalty)
print("Final Score:", final_score)


def get_confidence_level(score):

    if score >= 85:
        return "Very High"

    elif score >= 75:
        return "High"

    elif score >= 65:
        return "Moderate"

    elif score >= 50:
        return "Low"

    else:
        return "Very Low"

confidence = get_confidence_level(final_score)

print("Confidence:", confidence)