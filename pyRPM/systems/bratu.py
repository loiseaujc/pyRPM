"""
Implementation of the Bratu problem from the Schroff-Keller paper on RPM (1993).
"""

import numpy as np

from scipy.integrate import solve_ivp
from scipy.sparse import diags

from ..utils.pde import laplacian_1D


class Bratu():

    """
    Class implementing the solver for the 1D Bratu equation.

    ATTRIBUTES
    ----------

    nx  :   int (default : 128)
            Number of grid points to discretize the unit interval.

    l   :   float (default : 1.0)
            Control parameter of the Bratu problem.

    t   :   float (default : 0.1)
            Time horizon for the integration of the ODE problem.
    """

    def __init__(self, nx=128, l=1.0, t=0.1):
        """
        Initialization of the class.
        """

        # --> Number of grid points.
        self.nx = nx

        # --> Control parameter.
        self.l = l

        # --> Time horizon for the temporal integration.
        self.t = t

        # --> Uniform mesh for the unit interval.
        self.x = np.linspace(0, 1, nx+2)[1:-1]

        # --> Laplace operator on the unit interval.
        self.L = laplacian_1D(self.x)

    def _rhs(self, t, u):
        """
        Right-hand side of the Bratu ODE problem.
        """
        return self.L @ u + self.l * np.exp(u)

    def _jac(self, u):
        """
        Jacobian matrix of the Bratu problem.
        """
        return self.L + self.l * diags(np.exp(u))

    def solve(self, u):
        """
        This function integrate the Bratu nonlinear equation from time 0 to
        time t using u as the initial condition.
        """

        # --> Time interval over which integration is performed.
        tspan = (0, self.t)

        # --> Jacobian matrix of the Bratu problem for the implicit solver.
        def jac(t, u): return self._jac(u)

        # --> Integrate in time the Bratu ODE.
        output = solve_ivp(
            self._rhs,
            tspan,
            u,
            t_eval=np.asarray(tspan),
            method="BDF",
            jac=jac,
        )

        return output["y"][:, -1]
