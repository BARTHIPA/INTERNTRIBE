import pandas as pd

data = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107],
    'Salary': [55000, 75000, 62000, 58000, 80000, 60000, 59000],
    'YearsOfExperience': [2, 5, 4, 3, 6, 5, 2],
    'Age': [25, 28, 35, 26, 30, 34, 27]
})

mean_salary_by_dept = data.groupby('Department')['Salary'].mean()
print("1. Mean Salary by Department:\n", mean_salary_by_dept, "\n")

agg_results = data.groupby(['Department', 'Age']).agg({
    'Salary': ['mean', 'max', 'min'],
    'YearsOfExperience': 'mean'
})
print("2. Aggregation by Department and Age:\n", agg_results, "\n")

high_salary_departments = mean_salary_by_dept[mean_salary_by_dept > 60000]
print("3. Departments with Mean Salary > 60,000:\n", high_salary_departments, "\n")
def salary_range(series):
    return series.max() - series.min()

salary_range_by_dept = data.groupby('Department')['Salary'].agg(salary_range)
print("4. Salary Range by Department:\n", salary_range_by_dept)
