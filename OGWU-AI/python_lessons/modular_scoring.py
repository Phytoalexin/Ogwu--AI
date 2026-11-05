def calculate_team_strength(match): 
    return match["team_strength"] * 25

def calculate_recent_form(match):
    return match["recent_form"] * 20

def calculate_player_analysis(match):
    return match["player_analysis"] * 15

def calculate_home_advantage(match):
    return match["home_advantage"]  * 5 

def calculate_total_score(match):

    team_score = calculate_team_strength(match)

    form_score = calculate_recent_form(match)

    player_score = calculate_player_analysis(match)

    home_advantage = calculate_home_advantage(match)

    total = team_score + form_score + player_score + home_advantage

    return total


match = {
    "home_team": "Arsenal", 
    "away_team": "Chelsea",
    "team_strength": 8,
    "recent_form": 6,
    "player_analysis": 5,
    "home_advantage": 4
}

score = calculate_total_score(match)

print("Final Score:", score)