import pandas as pd
data = {
    "Name": ["John", "Jane", "Babu", "Peter", "Leju"],
    "Age": [25, 30, 35, 40, 55],
    "City": ["New York", "London", "Paris", "UK", "Germany"]
}
df = pd.DataFrame(data)
print("DataFrame Creation:")
print(data)
