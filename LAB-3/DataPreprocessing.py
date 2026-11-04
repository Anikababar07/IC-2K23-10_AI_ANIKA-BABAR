import pandas as pd
import numpy as np

# Create a dataset with missing values
data = {
    "Name": ["Anika", "Rahul", "Priya", "Aman", "Sneha"],
    "Age": [23, np.nan, 21, 24, np.nan],
    "Marks": [85, 78, np.nan, 88, 95]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Fill missing values with the mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nDataset After Handling Missing Values:")
print(df)