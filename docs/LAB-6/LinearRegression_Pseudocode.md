# Pseudocode: Linear Regression using PyTorch

BEGIN

    IMPORT PyTorch libraries

    CREATE training input data X
    CREATE training output data y

    CREATE a linear regression model

    DEFINE Mean Squared Error as the loss function
    DEFINE Stochastic Gradient Descent as the optimizer

    FOR each epoch from 1 to 100

        PERFORM forward pass
        CALCULATE loss

        RESET gradients
        PERFORM backpropagation

        UPDATE model parameters

    END FOR

    PROVIDE new input value

    PREDICT output using trained model

    DISPLAY the predicted value

END