import scipy.stats as stats
import numpy as np

population_mean = 100
sample_mean = 140
sample_std = 20
sample_size = 30
alpha = 0.05

t_statistic = (sample_mean - population_mean) / (sample_std / np.sqrt(sample_size))
df = sample_size - 1

p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), df))

print("IQ Medication T-Test Results:")
print(f"T-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < alpha:
    print("Reject the null hypothesis: Medication has a statistically significant effect.")
else:
    print("Fail to reject the null hypothesis: No significant effect detected.")
sample_mean_ci = 20
sample_std_ci = 3.5
sample_size_ci = 15
confidence = 0.95
df_ci = sample_size_ci - 1

t_critical = stats.t.ppf(1 - (1 - confidence) / 2, df_ci)

margin_error = t_critical * (sample_std_ci / np.sqrt(sample_size_ci))
lower_bound = sample_mean_ci - margin_error
upper_bound = sample_mean_ci + margin_error

print("95% Confidence Interval Estimate:")
print(f"Interval: ({lower_bound:.2f}, {upper_bound:.2f})")
