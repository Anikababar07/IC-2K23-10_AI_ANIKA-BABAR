import pandas as pd

# Create a simple dataset
data = {
    "Name": ["Anika", "Rahul", "Priya", "Aman", "Sneha"],
    "Age": [23, 22, 21, 24, 22],
    "Marks": [85, 78, 92, 88, 95]
}

# Create a DataFrame
df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

# Display basic information
print("\nDataset Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Find the student with maximum marks
top_student = df.loc[df["Marks"].idxmax()]

print("\nStudent with Highest Marks:")
print(top_student)