markets = [
    {
        "market": "Home Win",
        "score": 72
    },
    {
        "market": "Draw",
        "score": 51
    },
    {
        "market": "Away Win",
        "score": 46
    },
    {
        "market": "Over 1.5 Goals",
        "score": 84
    },
    {
        "market": "Over 2.5 Goals",
        "score": 68
    },
    {
        "market": "BTTS",
        "score": 76
    },
    {
        "market": "1H Over 0.5 Goals",
        "score": 88
    },
    {
        "market": "1H Over 1.5 Goals",
        "score": 54
    }
]


for market in markets:
    print(market["market"], "-", market["score"])


ranked_markets = sorted(
    markets,
    key=lambda market: market["score"],
    reverse=True
)

print()
print("===== MARKET RANKING =====")

for market in ranked_markets:
    print(f"{market['market']}: {market['score']}")


print()
print("===== MARKET RANKING =====")

for market in ranked_markets:
    print(f"{market['market']}: {market['score']}")