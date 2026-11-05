def evaluate_market(market, score, confidence):

    if confidence == "Very High":

        recommendation = "RECOMMENDED"
    elif confidence == "High":

        recommendation = "CONSIDER" 

    else:

        recommendation = "AVOID"
    return{
        "market": market,
        "score": score,
        "confidence": confidence,
        "recommendation": recommendation
    }
result = evaluate_market(
    "1H Over 0.5 Goals", 
    94,
    "Very High"
    
)

print(result)