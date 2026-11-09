# Loan Approval Prediction using Decision Tree

from sklearn.tree import DecisionTreeClassifier

# Training data
# [Income, Credit Score, Loan Amount]
X = [
    [30000, 650, 10000],
    [50000, 700, 15000],
    [60000, 750, 20000],
    [25000, 600, 12000],
    [80000, 800, 25000],
    [35000, 620, 18000]
]

# Output: 1 = Approved, 0 = Not Approved
y = [0, 1, 1, 0, 1, 0]

# Create and train the Decision Tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict loan approval for a new applicant
applicant = [[55000, 720, 18000]]
prediction = model.predict(applicant)

print("----- LOAN APPROVAL PREDICTION -----")

if prediction[0] == 1:
    print("Loan Status: Approved")
else:
    print("Loan Status: Not Approved")