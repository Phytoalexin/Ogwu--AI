market_groups = {
    "goals": [
        "Over 1.5 Goals",
        "Over 2.5 Goals",
        "BTTS" 
    ],

    "first_half": [
        "1H Over 0.5 Goals",
        "1H Over 1.5 Goals"
    ],

    "result": [
        "Home Win",
        "Draw",
        "Away Win"
    ]
}

def find_market_group(market):

    for group, markets in market_groups.items():

        if market in markets:
            return group

    return "umknown"

print(find_market_group("BTTS"))
print(find_market_group("Home Win"))
print(find_market_group("1H Over 0.5 Goals"))


def check_redundancy(markets):

    selected = []

    used_groups = []

    for market in markets:

        group = find_market_group(market["market"])

        if group not in used_groups:

            selected.append(market)

            used_groups.append(group)
    return selected 
