# Student Placement Prediction using Decision Tree

from sklearn.tree import DecisionTreeClassifier

# Training data
# [CGPA, Communication Skills Score]
X = [
    [6.5, 60],
    [7.0, 70],
    [8.0, 80],
    [8.5, 85],
    [5.5, 50],
    [7.5, 75]
]

# Output: 1 = Placed, 0 = Not Placed
y = [0, 1, 1, 1, 0, 1]

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict placement for a new student
student = [[7.8, 78]]
prediction = model.predict(student)

print("----- STUDENT PLACEMENT PREDICTION -----")

if prediction[0] == 1:
    print("Prediction: The student is likely to be Placed.")
else:
    print("Prediction: The student is not likely to be Placed.")