# Complexity Analysis: Linear Regression using PyTorch

## Time Complexity

The model is trained for a fixed number of epochs.

For each epoch, the model processes all training samples and performs forward and backward propagation.

The time complexity can be represented as:

**O(E × N × P)**

Where:

- E = Number of epochs
- N = Number of training samples
- P = Number of model parameters

For this simple linear regression model, P is constant. Therefore, the complexity mainly depends on the number of epochs and training samples.

## Space Complexity

The program stores the training data, model parameters, gradients, and intermediate results.

Therefore, the space complexity is:

**O(N + P)**

For this simple model, the number of parameters is constant.