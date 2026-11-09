import torch
import torch.nn as nn
from torchvision import models

# Load a pre-trained ResNet18 model
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.eval()

# Store gradients and feature maps
gradients = []
activations = []

# Hook functions
def forward_hook(module, input, output):
    activations.append(output)

def backward_hook(module, grad_input, grad_output):
    gradients.append(grad_output[0])

# Register hooks on the final convolution layer
target_layer = model.layer4[-1].conv2
target_layer.register_forward_hook(forward_hook)
target_layer.register_full_backward_hook(backward_hook)

# Create a sample input image
input_image = torch.randn(1, 3, 224, 224)

# Forward pass
output = model(input_image)

# Select the predicted class
predicted_class = output.argmax(dim=1).item()

# Backward pass
model.zero_grad()
output[0, predicted_class].backward()

# Calculate Grad-CAM
gradient = gradients[0]
activation = activations[0]

weights = torch.mean(gradient, dim=(2, 3), keepdim=True)
grad_cam = torch.sum(weights * activation, dim=1, keepdim=True)

# Apply ReLU and normalize
grad_cam = torch.relu(grad_cam)
grad_cam = grad_cam.squeeze().detach().numpy()

grad_cam = (grad_cam - grad_cam.min()) / (
    grad_cam.max() - grad_cam.min() + 1e-8
)

print("Predicted class index:", predicted_class)
print("Grad-CAM generated successfully!")
print("Grad-CAM shape:", grad_cam.shape)