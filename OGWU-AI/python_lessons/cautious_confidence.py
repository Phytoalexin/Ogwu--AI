def calculate_confidence(score, agreement):

    if score >= 400 and agreement >= 5:
        return "Very High"

    elif score >= 300 and agreement >=4:
        return "High"

    elif score >= 200 and agreement >= 3:
        return "Medium"

    else:
        return "Low"

score = 320
agreement = 4

confidence = calculate_confidence(score, agreement)

print("Score:" , score)
print("Evidence Ahreement:", agreement)
print("Confidence:", confidence)