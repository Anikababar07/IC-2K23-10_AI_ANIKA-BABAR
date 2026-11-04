import numpy as np

# Create NumPy arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

print("Array 1:", array1)
print("Array 2:", array2)

# Basic operations
print("\nAddition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Multiplication:", array1 * array2)
print("Division:", array1 / array2)

# Basic statistics
print("\nMean of Array 1:", np.mean(array1))
print("Maximum value:", np.max(array1))
print("Minimum value:", np.min(array1))
print("Sum of Array 1:", np.sum(array1))