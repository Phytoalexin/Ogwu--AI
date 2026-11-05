def calculate_team_strength(match):
    difference = match["home_strength"] - match["away_strength"]

    return difference

match = {
    "home_team": "Arsenal",
    "away_team": "Chelsea",
    "home_strength": 90,
    "away_strength": 90
}

strength_difference = calculate_team_strength(match)

print("Strength Difference:", strength_difference)