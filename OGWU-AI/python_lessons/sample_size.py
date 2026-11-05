def calculate_sample_quality(sample_size):

    if sample_size >= 50:
        return "Excellent"

    elif sample_size >= 30:
        return "Good"

    elif sample_size >= 15:
        return "Fair"

    else:
        return "Poor"

sample_size = 35 

quality = calculate_sample_quality(sample_size)

print("Sample Size:", sample_size)
print("Sample Quality:", quality)