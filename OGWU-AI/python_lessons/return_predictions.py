def predict_winner(match):

    if match["home_strength"] > match["away_strength"] :
        return match["home_team"]

    elif match["away_strength"] > match ["home_strength"]:
        return match ["away_team"]

    else: 
        return "Draw" 

match = {

    "home_team" : "Liverpool",
    "away_team" : "Arsenal",
    "home_strength": 90,
    "away_strength": 91
}

prediction = predict_winner(match)

print("Prediction:", prediction)