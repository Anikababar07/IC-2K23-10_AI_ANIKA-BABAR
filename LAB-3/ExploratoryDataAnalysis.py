import pandas as pd

# Create a sample dataset
data = {
    "Name": ["Anika", "Rahul", "Priya", "Aman", "Sneha"],
    "Age": [23, 22, 21, 24, 22],
    "Marks": [85, 78, 92, 88, 95]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())