# Algorithm: Linear Regression using PyTorch

1. Start the program.
2. Import the PyTorch libraries.
3. Create the training input data X and output data y.
4. Create a linear regression model using a linear layer.
5. Define Mean Squared Error as the loss function.
6. Define Stochastic Gradient Descent as the optimizer.
7. Repeat the training process for a fixed number of epochs:
   - Perform a forward pass to generate predictions.
   - Calculate the loss between predictions and actual values.
   - Reset the gradients.
   - Perform backpropagation to calculate gradients.
   - Update the model parameters using the optimizer.
8. Provide a new input value to the trained model.
9. Display the predicted output.
10. Stop the program.