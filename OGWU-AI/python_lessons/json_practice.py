match_data = {
    "competition": "Premier League",
    "home_team": "Arsenal",
    "away_team": "Chelsea",
    "home_score": 2,
    "away_score": 1
}

print(match_data)


print()
print(match_data["competition"])
print(match_data["home_team"])
print(match_data["away_team"])
print(match_data["home_score"])
print(match_data["away_score"])


print()
print("========== OGWU AI ==========")
print(f"Competition: {match_data['competition']}")
print(f"Match: {match_data['home_team']} vs {match_data['away_team']}")
print(
    f"Score: {match_data['home_score']} - "
    f"{match_data['away_score']}"
)
print("==============================")