def adjust_for_correlation(score, correlation):

    adjusted_score = score - correlation 

    return adjusted_score

score = 95
correlation = 7

adjusted_score = adjust_for_correlation(score, correlation)

print("Original Score:", score)
print("Correational Penalty:", correlation)
print("Adjusted Score:", adjusted_score)