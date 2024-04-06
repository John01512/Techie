import numpy as np

class Perceptron:
    def __init__(self, learning_rate, epochs):
        """
        Initialize the Perceptron model.

        Parameters:
        learning_rate (float): The learning rate for updating weights during training.
        epochs (int): The number of training epochs.
        """
        self.weights = None  # Initialize weights to be determined during training
        self.bias = None  # Initialize bias term to be determined during training
        self.learning_rate = learning_rate  # Set the learning rate for the model
        self.epochs = epochs  # Set the number of training epochs

    def activation(self, z):
        """
        Activation function for the perceptron model.

        Parameters:
        z (float): The input to the activation function.

        Returns:
        int: 1 if z >= 0, otherwise 0.
        """
        return np.heaviside(z, 0)

    def fit(self, X, y):
        """
        Fit the Perceptron model to the training data.

        Parameters:
        X (array-like): The training input samples.
        y (array-like): The target values.

        Returns:
        tuple: The learned weights and bias.
        """
        n_features = X.shape[1]  # Get the number of features in the input data
        self.weights = np.zeros((n_features,))  # Initialize weights as zeros
        self.bias = 0  # Initialize bias as zero

        # Iterate over each training epoch
        for epoch in range(self.epochs):
            # Iterate over each training sample
            for i in range(len(X)):
                z = np.dot(X[i], self.weights) + self.bias  # Compute the weighted sum
                y_pred = self.activation(z)  # Apply activation function to the sum

                # Update weights and bias using the perceptron learning rule
                self.weights = self.weights + self.learning_rate * (y[i] - y_pred) * X[i]
                self.bias = self.bias + self.learning_rate * (y[i] - y_pred)

        return self.weights, self.bias

    def predict(self, X):
        """
        Predict the output for input samples using the trained perceptron model.

        Parameters:
        X (array-like): The input samples.

        Returns:
        array-like: Predicted binary labels (0 or 1).
        """
        z = np.dot(X, self.weights) + self.bias  # Compute the weighted sum
        return self.activation(z)  # Apply activation function and return the predictions

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()
X = iris.data[:, (0, 1)]  # Selecting only the first two features for simplicity
y = (iris.target == 0).astype(int)  # Convert the target labels to binary (0 or 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Create an instance of the Perceptron model with specified learning rate and epochs
perceptron = Perceptron(0.001, 100)

# Train the Perceptron model on the training data
perceptron.fit(X_train, y_train)

# Predict the labels for the test data
pred = perceptron.predict(X_test)

# Print the predictions
print("Predictions:", pred)