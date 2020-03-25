"""
Basic implementation of the Newton method.
"""

import numpy as np

from scipy.sparse.linalg import spsolve

def newton_solver(fun, x, jac=None, maxiter=100, tol=1e-10, linear_solver=None):
    """
    Basic implementation of the Newton method.
    """

    # -->
    if jac is None:
        raise NotImplementedError

    # -->
    for i in range(maxiter):

        # --> Evaluate the Jacobian matrix at the current point.
        J = jac(x)

        # --> Solve the linear system.
        dx = -spsolve(J, fun(x))

        # --> Update the solution.
        x += dx

        # --> Check for the residual.
        if np.linalg.norm(fun(x)) < tol:
            print("Newton converged in {0} iterations.".format(i))
            break

    return x
