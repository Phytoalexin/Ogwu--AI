home_team = input("Home Team: ")
away_team = input("Away Team: ")

home_strength = int(input("Home Team Strength (1-100): "))
away_strength = int(input("Away Team Strength (1-100): "))

print()

if home_strength > away_strength:
    print(f"Prediction: {home_team} to Win")

if away_strength > home_strength:
    print(f"Prediction: {away_team} to Win")

if home_strength == away_strength: 
    print("Prediction: Draw")

