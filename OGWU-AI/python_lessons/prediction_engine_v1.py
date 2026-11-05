print("=============== OGWU AI ===============")

competition = input("Competition: ")
home_team = input("Home Team: ")
away_team = input("Away Team: ")
home_strength = int(input(f"{home_team} Strength: "))
away_strength = int(input(f"{away_team} Strength: "))
difference = abs(home_strength - away_strength)

print()

print("================ RESULT ===============")
print(f"Competition: {competition}")
print(f"Match: {home_team} vs {away_team}")

print()
if home_strength > away_strength:
    print(f"Prediction: {home_team} to Win")
elif away_strength > home_strength:
    print(f"Prediction: {away_team} to Win") 
else: 
    print("Prediction: Draw")

print()
if difference >= 20:
    print("Confidence: Very High")
elif difference >=10:
    print("Confidence: High")
elif difference >=5:
    print("Confidence: Medium")
else:
    print("Confidence: Low")            


print("========================================")           