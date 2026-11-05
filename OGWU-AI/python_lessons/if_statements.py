home_team = input("Home Team: ")
away_team = input("Away Team: ")

home_strength = int(input("Home Strength (1-100): "))
away_strength = int(input("Away Strength (1-100): "))

print()

if home_strength > away_strength:
    print(f"Predicition: {home_team} is stronger.")

elif away_strength > home_strength:
    print(f"Prediction: {home_team} is stronger.")

else: 
    print("Prediction: Both teams are evenly matched.")    