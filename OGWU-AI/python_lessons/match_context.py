def get_competition_weight(competition_type):

    if competition_type == "Champions League Knockout":
        return 1.00

    elif competition_type == "League Match":
        return 0.90

    elif competition_type == "Cup Match":
        return 0.85

    elif competition_type == "Friendly":
        return 0.60

    else:
        return 0.50


competition = "League Match"

weight = get_competition_weight(competition)

print("Competition:", competition)
print("Context Weight:", weight)

def get_motivation_weight(motivation):

    if motivation == "Very High":
        return 1.00

    elif motivation == "High":
        return 0.90

    elif motivation == "Medium":
        return 0.75

    else:
        return 0.60


motivation = "Very High"

motivation_weight = get_motivation_weight(motivation)

print("Motivation:", motivation)
print("Motivation Weight:", motivation_weight)


def calculate_context_weight(competition_weight, motivation_weight):

    return competition_weight * motivation_weight


competition_weight = get_competition_weight("League Match")
motivation_weight = get_motivation_weight("High")

context_weight = calculate_context_weight(
    competition_weight,
    motivation_weight
)

print("Competition Weight:", competition_weight)
print("Motivation Weight:", motivation_weight)
print("Overall Context Weight:", context_weight)