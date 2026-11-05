markets = [
    {"market": "Home Win", "score": 68},
    {"market": "Over 2.5 Goals", "score" : 87},
    {"market": "BTTS", "score": 91},
    {"market": "1H Over 0.5 Goals", "score": 95}
]

markets.sort(key=lambda market: market["score"], reverse=True)

print("================ OGWU AI ================")
print()

for market in markets:
    print(f"{market['market']}: {market['score']}")

print()
print("==========================================")