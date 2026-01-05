import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    point_a = np.array(x)
    point_b = np.array(y)
    return np.linalg.norm(point_a - point_b)