

def analyze_match(match):
    print("-----------------------------------")

    print(match["competition"])
    print(f"{match['home_team']} vs {match['away_team']}")

    if match["home_strength"] > match["away_strength"]:
        print(f"Prediction: {match['home_team']} to Win")
    elif match["away_strength"] > match["home_strength"]:
        print(f"Prediction: {match['away_team']} to Win")

    else:
        print("Prediction: Draw")
        print("-----------------------------------")

weekend_matches = [
        {
            "competition": "Premier League",
            "home_team": "Liverpool",
            "away_team": "Arsenal",
            "home_strength": 90,
            "away_strength": 91

        },
        {
            "competition": "Serie A",
            "home_team": "Inter",
            "away_team": "Juventus",
            "home_strength": 92,
            "away_strength": 89
        },
        {
            "competition": "Bundesliga",
            "home_team": "Bayern Munich",
            "away_team": "Borussia Dortmund", 
            "home_strength": 94,
            "away_strength": 88
        
        }
    ]

for match in weekend_matches:
        analyze_match(match)