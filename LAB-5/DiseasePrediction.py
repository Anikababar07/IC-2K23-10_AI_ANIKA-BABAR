# Disease Prediction using Decision Tree

from sklearn.tree import DecisionTreeClassifier

# Training data
# [Fever, Cough, Headache]
# 1 = Yes, 0 = No
X = [
    [1, 1, 1],
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1],
    [1, 0, 0],
    [0, 0, 0]
]

# Disease labels
y = ["Flu", "Flu", "Cold", "Migraine", "Fever", "Healthy"]

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict disease for a new patient
patient = [[1, 1, 1]]
prediction = model.predict(patient)

print("----- DISEASE PREDICTION -----")
print("Predicted Disease:", prediction[0])