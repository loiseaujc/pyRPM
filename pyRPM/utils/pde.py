"""
Utilities for partial differential equations.
"""

# -->
import numpy as np

# -->
from scipy.sparse import diags


def laplacian_1D(x, bc="dirichlet"):
    """
    This function constructs the finite-difference approximation of the
    one-dimensional Laplace operator.

    Parameters
    ----------
    x : numpy array-like, shape (n,)
        One-dimensional mesh. Assumes the mesh is uniform.

    Returns
    -------
    L : scipy sparse matrix, shape (n, n)
        Finite-difference approximation of the 1D Laplace operator.

    """

    # -->
    dx = x[1] - x[0]

    n = len(x)

    # -->
    d2 = [np.ones(n-1), -2*np.ones(n), np.ones(n-1)]

    # -->
    L = diags(d2, [-1, 0, 1]) / dx**2

    return L
