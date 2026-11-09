import torch
from torchvision import models

# Load pre-trained ResNet18
weights = models.ResNet18_Weights.DEFAULT
model = models.resnet18(weights=weights)

# Set model to evaluation mode
model.eval()

# Create a sample image tensor
input_image = torch.randn(1, 3, 224, 224)

# Perform classification
with torch.no_grad():
    output = model(input_image)

# Get predicted class
predicted_class = output.argmax(dim=1).item()

print("ResNet-based Image Classification")
print("Predicted class index:", predicted_class)