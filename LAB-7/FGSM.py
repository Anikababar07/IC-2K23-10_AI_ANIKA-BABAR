import torch
import torch.nn as nn

# Create a simple neural network
model = nn.Sequential(
    nn.Linear(10, 20),
    nn.ReLU(),
    nn.Linear(20, 2)
)

# Loss function
criterion = nn.CrossEntropyLoss()

# Create sample input
data = torch.randn(1, 10, requires_grad=True)
target = torch.tensor([1])

# Forward pass
output = model(data)
loss = criterion(output, target)

# Calculate gradients
model.zero_grad()
loss.backward()

# FGSM attack
epsilon = 0.1
data_grad = data.grad.data

perturbed_data = data + epsilon * data_grad.sign()

print("Original input:")
print(data.detach())

print("\nPerturbed input after FGSM attack:")
print(perturbed_data.detach())

print("\nFGSM attack completed successfully!")