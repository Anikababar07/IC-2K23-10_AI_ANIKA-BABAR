# Decision Tree Visualization

from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

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

# Visualize the Decision Tree
plt.figure(figsize=(10, 6))

plot_tree(
    model,
    feature_names=["CGPA", "Communication Skills"],
    class_names=["Not Placed", "Placed"],
    filled=True
)

plt.title("Student Placement Decision Tree")
plt.show()