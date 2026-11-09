import torch

# Create a tensor with gradient tracking enabled
x = torch.tensor(3.0, requires_grad=True)

# Perform a mathematical operation
y = x ** 2 + 2 * x + 1

# Compute gradients
y.backward()

# Display the results
print("Value of x:", x.item())
print("Value of y:", y.item())
print("Gradient of y with respect to x:", x.grad.item())