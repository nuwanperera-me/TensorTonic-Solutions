import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v = np.asarray(v, dtype=float)
    orig_shape = v.shape
    
    if v.ndim == 1:
        v = v[np.newaxis, :]
    
    norms = np.linalg.norm(v, axis=1, keepdims=True)
    
    tol = 1e-10
    norms_safe = np.where(norms > tol, norms, 1.0)
    v_norm = v / norms_safe
    v_norm = np.where(norms > tol, v_norm, 0.0)
    
    if orig_shape == (3,):
        return v_norm[0]
    return v_norm.reshape(orig_shape)