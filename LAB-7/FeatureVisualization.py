import torch
import torch.nn as nn

# Create a simple neural network
model = nn.Sequential(
    nn.Linear(5, 10),
    nn.ReLU(),
    nn.Linear(10, 3)
)

# Input data
input_data = torch.randn(1, 5)

# Store intermediate features
features = []

# Hook function
def get_features(module, input, output):
    features.append(output.detach())

# Register hook on the first layer
handle = model[0].register_forward_hook(get_features)

# Forward pass
output = model(input_data)

# Remove hook
handle.remove()

print("Input Data:")
print(input_data)

print("\nExtracted Features:")
print(features[0])

print("\nFinal Model Output:")
print(output)

print("\nFeature visualization completed successfully!")