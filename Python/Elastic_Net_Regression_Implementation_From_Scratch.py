import numpy as np

class ElasticNetRegression:
    def __init__(self, alpha=1.0, l1_ratio=0.5, max_iter=1000, learning_rate=0.01):
        self.alpha = alpha  # Regularization parameter (λ)
        self.l1_ratio = l1_ratio  # L1 ratio (0 to 1)
        self.max_iter = max_iter  # Maximum number of iterations
        self.learning_rate = learning_rate  # Learning rate for gradient descent

    def fit(self, X, y):
        # Add a column of ones for the bias term
        X = np.column_stack((np.ones(len(X)), X))
        m, n = X.shape
        self.theta = np.random.rand(n)  # Initialize coefficients with random values

        for _ in range(self.max_iter):
            gradient = self.compute_gradient(X, y)
            self.theta -= self.learning_rate * gradient

    def compute_gradient(self, X, y):
        m = len(y)
        y_pred = X @ self.theta
        error = y_pred - y

        # Compute gradients for L1 and L2 regularization
        l1_gradient = self.l1_ratio * np.sign(self.theta)
        l2_gradient = (1 - self.l1_ratio) * self.theta

        gradient = (1 / m) * X.T @ error + self.alpha * (l1_gradient + l2_gradient)

        return gradient

    def predict(self, X):
        # Add a column of ones for the bias term
        X = np.column_stack((np.ones(len(X)), X))

        # Make predictions
        return X @ self.theta

# Example usage:
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    X = 2 * np.random.rand(100, 3)
    y = 4 + X[:, 0] + 3 * X[:, 1] + 2 * X[:, 2] + np.random.randn(100)

    # Create and fit the Elastic Net Regression model
    elastic_net = ElasticNetRegression(alpha=1.0, l1_ratio=0.5)
    elastic_net.fit(X, y)

    # Make predictions
    y_pred = elastic_net.predict(X)

    # Print the coefficients
    print("Coefficients:", elastic_net.theta[1:])
    print("Intercept:", elastic_net.theta[0])
