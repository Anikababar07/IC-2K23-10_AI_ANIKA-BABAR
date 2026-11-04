import matplotlib.pyplot as plt

# Student data
students = ["Anika", "Rahul", "Priya", "Aman", "Sneha"]
marks = [85, 78, 92, 88, 95]

# Create a bar chart
plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# Display the graph
plt.show()