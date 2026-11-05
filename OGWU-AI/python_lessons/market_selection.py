markets = [
    {
        "name": "1H Over 0.5 Goals",
        "score": 94,
        "data_quality": "Excellent",
        "sample_size": 50
    },
    {
        "name": "Over 1.5 Goals",
        "score": 91,
        "data_quality": "Excellent",
        "sample_size": 50
    },
    {
        "name": "BTTS",
        "score": 86,
        "data_quality": "Good",
        "sample_size": 35
    },
    {
        "name": "Home Win",
        "score": 82,
        "data_quality": "Fair",
        "sample_size": 12
    },
    {
        "name": "Away Win",
        "score": 44,
        "data_quality": "Good",
        "sample_size": 40
    }
]

MINIMUM_SCORE = 65

def passes_score_filter(score):

    if score >= MINIMUM_SCORE:
        return True

    else:
        return False


print(passes_score_filter(80))
print(passes_score_filter(50))


qualified_markets = []

for market in markets:

    if passes_score_filter(market["score"]):

        qualified_markets.append(market)


print()
print("===== QUALIFIED MARKETS =====")

for market in qualified_markets:
    print(market["name"], "-", market["score"])



def passes_data_quality_filter(quality):

    if quality == "Excellent":
        return True

    elif quality == "Good":
        return True

    else:
        return False

qualified_markets = []

for market in markets:

    score_ok = passes_score_filter(market["score"])

    quality_ok = passes_data_quality_filter(
        market["data_quality"]
    )

    if score_ok and quality_ok:

        qualified_markets.append(market)