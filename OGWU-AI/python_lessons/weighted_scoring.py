def calculate_total_score(match): 

    team_strength_score = match["team_strength"] * 25

    recent_form_score = match["recent_form"] * 20

    player_score = match["player_analysis"] * 15

    total_score = (
        team_strength_score
        + recent_form_score
        + player_score
    )

    return total_score

match = {
    "home_team": "Arsenal",

    "away_team": "Chelsea",

    "team_strength": 4,

    "recent_form": 6,

    "player_analysis": 9
}

score = calculate_total_score(match)

print("Total Score:", score)
