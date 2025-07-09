
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

data = stats.norm.rvs(loc=50, scale=20, size=100)

df = pd.DataFrame(data, columns=['values'])

df.plot.density()
plt.title("Density Plot of Normally Distributed Data")
plt.xlabel("Values")
plt.ylabel("Density")
plt.grid(True)
plt.show()

mean = df['values'].mean()
median = df['values'].median()

print("Mean:", mean)
print("Median:", median)
