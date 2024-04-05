import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

class Perceptron:
    def __init__(self, learning_rate, epochs):
        self.weights = None
        self.bias = None
        self.learning_rate = learning_rate
        self.epochs = epochs
    
    def activation(self, z):
        return np.heaviside(z, 0)
    
    def fit(self, X, y):
        n_features = X.shape[1]
        self.weights = np.zeros((n_features,))
        self.bias = 0
        
        for epoch in range(self.epochs):
            for i in range(len(X)):
                z = np.dot(X[i], self.weights) + self.bias
                y_pred = self.activation(z)
                self.weights = self.weights + self.learning_rate * (y[i] - y_pred) * X[i]
                self.bias = self.bias + self.learning_rate * (y[i] - y_pred)
        
        return self.weights, self.bias
    
    def predict(self, X):
        z = np.dot(X, self.weights) + self.bias
        return self.activation(z)

# Load Iris dataset
iris = load_iris()
X = iris.data[:, (0, 1)]
y = (iris.target == 0).astype(int)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Instantiate Perceptron model
perceptron = Perceptron(learning_rate=0.001, epochs=100)

# Train Perceptron model
perceptron.fit(X_train, y_train)

# Predict on test data
pred = perceptron.predict(X_test)
print("Predictions:", pred)
