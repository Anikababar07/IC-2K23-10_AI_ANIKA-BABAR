import torch

# Create tensors
tensor1 = torch.tensor([1, 2, 3, 4])
tensor2 = torch.tensor([5, 6, 7, 8])

# Perform basic operations
addition = tensor1 + tensor2
multiplication = tensor1 * tensor2

# Create a tensor and reshape it
tensor3 = torch.arange(1, 7)
reshaped_tensor = tensor3.reshape(2, 3)

# Display the results
print("Tensor 1:", tensor1)
print("Tensor 2:", tensor2)

print("\nAddition:", addition)
print("Multiplication:", multiplication)

print("\nOriginal Tensor:", tensor3)
print("\nReshaped Tensor:")
print(reshaped_tensor)

print("\nShape:", reshaped_tensor.shape)
print("Data Type:", reshaped_tensor.dtype)