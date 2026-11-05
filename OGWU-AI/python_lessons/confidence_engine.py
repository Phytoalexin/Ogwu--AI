def calculate_team_strength(match):
    return match["team_strength"] * 25

def calculate_recent_form(match):
    return match["recent_form"] * 20

def calculate_player_analysis(match):
    return match["player_analysis"] * 15

def calculate_home_advantage(match):
    return match["home_advantage"] * 5

def calculate_total_score(match):

    team_score = calculate_team_strength(match)

    form_score = calculate_recent_form(match)

    player_score = calculate_player_analysis(match)

    home_score = calculate_home_advantage(match)

    total = team_score + form_score + player_score + home_score

    return total

def calculate_confidence(score): 
    if score >= 400:
        return "Very High"

    elif score >= 300:
        return "High"

    elif score >=200:
        return "Medium"

    else:
        return "Low"


match = {
    "home_team": "Arsenal",
    "away_team": "Chelsea",

    "team_strength": 3,
    "recent_form": 9,
    "player_analysis": 5,
    "home_advantage": 4
}    

score = calculate_total_score(match)

confidence = calculate_confidence(score)

print("============= OGWU AI ==============")
print()
print(f"Match: {match['home_team']} vs {match['away_team']}")
print(f"Score: {score}")
print(f"Confidence: {confidence}")
print()
print("=====================================")