import torch
import torch.nn as nn
import torch.optim as optim

# Training data
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# Create a Linear Regression model
model = nn.Linear(1, 1)

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Train the model
for epoch in range(100):
    # Forward pass
    predictions = model(X)

    # Calculate loss
    loss = criterion(predictions, y)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Make a prediction
new_input = torch.tensor([[5.0]])
prediction = model(new_input)

print("----- LINEAR REGRESSION USING PYTORCH -----")
print("Prediction for x = 5:", prediction.item())