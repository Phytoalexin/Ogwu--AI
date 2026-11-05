
def welcome(): 

    print()
    print("===============================")
    print( "                OGWU AI")
    print("Football Prediction Engine")
    print("===============================")
    print()

def get_match():

    competition = input("Competition: ")

    home_team = input("Home Team: ")

    away_team = input("Away Team: ")

    print()
    
    print("Match Selected")
    print(f"{home_team} vs {away_team}")

    print()

    return competition, home_team, away_team

welcome()

competition, home_team, away_team = get_match()

print("Competition:", competition)

print("Home:", home_team)

print("Away:", away_team)


