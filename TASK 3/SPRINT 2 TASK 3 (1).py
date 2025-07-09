import pandas as pd
from scipy.stats import skew, kurtosis

df = pd.read_excel(r'C:/Users/Barthipa Sarathy/Downloads/Titanic.xlsx')

mean_age = df['Age'].mean()

median_fare = df['Fare'].median()

mode_embarked = df['Embarked'].mode()[0]

fare_stats_by_class = df.groupby('Pclass')['Fare'].agg(['mean', 'median'])
fare_mode_by_class = df.groupby('Pclass')['Fare'].agg(lambda x: x.mode()[0])

mean_sibsp = df['SibSp'].mean()
median_sibsp = df['SibSp'].median()

fare_skewness = skew(df['Fare'].dropna())
fare_skew_type = 'positively skewed' if fare_skewness > 0 else 'negatively skewed'

age_kurtosis = kurtosis(df['Age'].dropna())
age_kurtosis_type = 'leptokurtic (peaked)' if age_kurtosis > 0 else 'platykurtic (flat)'

parch_skewness = skew(df['Parch'].dropna())
parch_distribution = 'symmetrically distributed' if abs(parch_skewness) < 0.5 else 'not symmetric'

survived_skewness = skew(df['Survived'].dropna())
survived_kurtosis = kurtosis(df['Survived'].dropna())
survived_normality = 'possibly normal' if abs(survived_skewness) < 0.5 and abs(survived_kurtosis) < 3 else 'not normally distributed'
comparison = {
    'Fare': {
        'skewness': fare_skewness,
        'kurtosis': kurtosis(df['Fare'].dropna())
    },
    'Age': {
        'skewness': skew(df['Age'].dropna()),
        'kurtosis': age_kurtosis
    }
}
print(f"Mean Age: {mean_age:.2f}")
print(f"Median Fare: {median_fare:.2f}")
print(f"Most common embarkation point: {mode_embarked}")
print("Fare stats by class:\n", fare_stats_by_class)
print("Fare mode by class:\n", fare_mode_by_class)
print(f"Mean SibSp: {mean_sibsp:.2f}, Median SibSp: {median_sibsp}")
print(f"Fare Skewness: {fare_skewness:.2f} ({fare_skew_type})")
print(f"Age Kurtosis: {age_kurtosis:.2f} ({age_kurtosis_type})")
print(f"Parch Skewness: {parch_skewness:.2f} ({parch_distribution})")
print(f"Survived Skewness: {survived_skewness:.2f}, Kurtosis: {survived_kurtosis:.2f} ({survived_normality})")
print("Comparison (Fare vs Age):", comparison)
