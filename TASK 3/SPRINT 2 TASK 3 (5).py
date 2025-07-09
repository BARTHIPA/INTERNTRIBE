import scipy.stats as stats
import numpy as np

population_mean = 168
sample_mean = 169.5
population_std = 3.9
sample_size = 36
alpha = 0.05  

z = (sample_mean - population_mean) / (population_std / np.sqrt(sample_size))

p_value = 2 * (1 - stats.norm.cdf(abs(z)))

print("Hypothesis Testing Results:")
print(f"Z-score: {z:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < alpha:
    print("Reject the null hypothesis: There's enough evidence to suggest a difference.")
else:
    print("Fail to reject the null hypothesis: No significant difference detected.")



sample_mean_ci = 32
population_std_ci = 5.6
sample_size_ci = 40
confidence_levels = [0.80, 0.90, 0.98]

print("Confidence Intervals for Exam Scores:")
for confidence in confidence_levels:
    z_critical = stats.norm.ppf(1 - (1 - confidence) / 2)
    margin_of_error = z_critical * (population_std_ci / np.sqrt(sample_size_ci))
    lower_bound = sample_mean_ci - margin_of_error
    upper_bound = sample_mean_ci + margin_of_error

    print(f"{int(confidence * 100)}% Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")
