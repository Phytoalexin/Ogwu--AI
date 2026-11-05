def classify_market(score):

    if score >= 85:
        return "Strong"

    elif score >= 75:
        return "Good"

    elif score >= 65:
        return "Caution"

    else:
        return "No Bet"


score = 88

classification = classify_market(score)

print("Score:", score)
print("Classification:", classification)


markets = [
    {
        "name": "1H Over 0.5 Goals",
        "type": "Goals",
        "score": 94
    },
    {
        "name": "Over 1.5 Goals",
        "type": "Goals",
        "score": 91
    },
    {
        "name": "BTTS",
        "type": "Goals",
        "score": 86
    },
    {
        "name": "Home Win",
        "type": "Result",
        "score": 82
    },
    {
        "name": "Away Win",
        "type": "Result",
        "score": 44
    }
]

for market in markets:

    classification = classify_market(market["score"])

    print(
        market["name"],
        "-",
        market["score"],
        "-",
        classification
    )

classification = classify_market(market["score"])

print()
print("===== OGWU RECOMMENDATION =====")
print("Market:", market["name"])
print("Score:", market["score"])
print("Classification:", classification)