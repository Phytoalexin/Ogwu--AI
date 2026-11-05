def calculate_data_quality(data_points):

    if data_points >= 90:
        return "Excellent"

    elif data_points >= 70:
        return "Good"

    elif data_points >= 50:
        return "Fair"

    else:
        return "Poor"

data_points = 85

quality = calculate_data_quality(data_points)

print("Data Quality:", quality)


def adjust_for_data_quality(score, qulaity):

    if quality == "Excellent":
        penalty = 0

    elif quality == "Good":
        penalty = 5

    elif quality == "Fair":
        penalty = 15

    else: 
        penalty = 30

    adjusted_score = score - penalty

    if adjusted_score < 40:
        adjusted_score =40

    return adjusted_score

score = 90
quality = "Good"

adjusted_score = adjust_for_data_quality(score, quality)

print("Original Score:", score)
print("Data Quality:", quality)
print("Adjusted Score:", adjusted_score)