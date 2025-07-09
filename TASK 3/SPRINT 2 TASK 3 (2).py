import pandas as pd
import numpy as np

Exp = [1, 2, 3, 4, 5]
Salary = [1000, 2500, 4000, 5000, 7000]

mean_exp = np.mean(Exp)
std_exp = np.std(Exp)
mean_salary = np.mean(Salary)
std_salary = np.std(Salary)

standardized_exp = [(x - mean_exp) / std_exp for x in Exp]
standardized_salary = [(x - mean_salary) / std_salary for x in Salary]

df = pd.DataFrame(
    [Exp, Salary, standardized_exp, standardized_salary],
    index=["Exp", "Salary", "Std_Exp", "Std_Salary"]
)

print("Standardized Data Table:\n", df)
print("\nVerification of Standardization:")
print("Mean of Std_Exp:", np.mean(standardized_exp))
print("Std Dev of Std_Exp:", np.std(standardized_exp))
print("Mean of Std_Salary:", np.mean(standardized_salary))
print("Std Dev of Std_Salary:", np.std(standardized_salary))
