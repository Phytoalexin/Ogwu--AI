today_matches = [
    {
        "competition": "Premier League",
        "home_team": "Arsenal",
        "away_team": "Chelsea",
        "stadium": "Emirates Stadium"
    }, 
    {
        "competition": "La Liga",
        "home_team": "Barcelona",
        "away_team": "Real Madrid",
        "stadium": "Camp Nou"
    }

]

print(today_matches)
print(today_matches[0]["home_team"])
print(today_matches[0]["away_team"])
print()


print(today_matches[1]["home_team"])
print(today_matches[1]["away_team"])


for match in today_matches:
    print("----------------------------")
    print(match["competition"])
    print(f"{match['home_team']} vs {match['away_team']}")
    print(match["stadium"])



    #Assignment

    weekend_matches = [
        {
            "competition": "Premier League",
            "home_team": "Liverpool",
            "away_team": "Arsenal",
            "stadium": "Anfield",
            "home_strength": 90,
            "away_strength": 91
        },
        {
            "competition": "Serial A",
            "home_team": "Inter Milan",
            "away_team": "Juventus",
            "stadium": "San Siro",
            "home_strength": 92,
            "away_strength": 89

        },  
        {
            "competition": "Bundesliga",
             "home_team": "Bayern Munich",
             "away_team": "Borussia Dortmund",
             "stadium": "Allianz Arena",
             "home_strength": 94,
             "away_strength": 88
        }
    ]

    for match in weekend_matches:
        print("----------------------------")
        print(match["competition"])
        print(f"{match['home_team']} vs {match ['away_team']}")
        print(match["home_strength"])
        print(match["away_strength"])
