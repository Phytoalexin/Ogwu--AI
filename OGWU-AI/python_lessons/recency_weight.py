def calculate_recency_weight(days_ago):

    if days_ago <= 7:
        return 1.00

    elif days_ago <= 14:
        return 0.90

    elif days_ago <= 30:
        return 0.75

    elif days_ago <= 60:
        return 0.60

    else:
        return 0.40



print(calculate_recency_weight(3))
print(calculate_recency_weight(10))
print(calculate_recency_weight(25))
print(calculate_recency_weight(45))
print(calculate_recency_weight(100))


def apply_recency(score, weight):

    return score * weight

score = 90
weight = calculate_recency_weight(10)

adjusted_score = apply_recency(score, weight)

print("Original Score:", score)
print("Recency Weight:", weight)
print("Recency Adjusted Score:", adjusted_score)


def calculate_relevance_weight(relevance):

    if relevance == "Very High":
        return 1.00

    elif relevance == "High":
        return 0.85

    elif relevance == "Medium":
        return 0.70

    else:
        return 0.50