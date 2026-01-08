import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    x = np.atleast_1d(np.asarray(x, dtype=np.float64))
    return np.maximum(0.0, x)