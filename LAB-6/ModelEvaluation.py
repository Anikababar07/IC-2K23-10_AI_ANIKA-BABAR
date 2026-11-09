import torch
import torch.nn as nn
import torch.optim as optim

# Training data
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# Create the model
model = nn.Linear(1, 1)

# Loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Train the model
for epoch in range(100):
    predictions = model(X)
    loss = criterion(predictions, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Evaluation mode
model.eval()

# Test data
test_X = torch.tensor([[5.0], [6.0]])
test_y = torch.tensor([[10.0], [12.0]])

# Evaluate the model without calculating gradients
with torch.no_grad():
    predictions = model(test_X)
    test_loss = criterion(predictions, test_y)

print("----- MODEL EVALUATION -----")
print("Predictions:")
print(predictions)
print("Test Loss:", test_loss.item())