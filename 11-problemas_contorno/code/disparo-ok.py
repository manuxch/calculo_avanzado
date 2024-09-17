#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import bisect
plt.style.use('../../utils/clases.mplstyle')

def f(x, y):
    f = np.zeros(2)
    f[0] = y[1]
    f[1] = 12 * x - 4 * y[0]
    return f

def residuo(r, a, b, beta):
    x = np.linspace(a, b, 100)
    sol = solve_ivp(f, [a, b], [1, r], dense_output=True)
    z = sol.sol(x)
    resid = z.T[-1, 0] - beta
    return resid

x_a, x_b = 0.0, 1.0
n_points = 100
beta = 3.5
x = np.linspace(x_a, x_b, n_points)

sol_1 = solve_ivp(f, [x_a, x_b], [1.0, 4.0], dense_output=True)
y_1 = sol_1.sol(x)
sol_2 = solve_ivp(f, [x_a, x_b], [1.0, 6.0], dense_output=True)
y_2 = sol_2.sol(x)
plt.plot(x, y_1.T[:, 0], '-.k', label=r"$r_0 = 4.0$")
plt.plot(x, y_2.T[:, 0], '--k', label=r"$r_1 = 6.0$")
plt.plot([0, 1], [1.0, 3.5], 'go')
plt.plot([x[-1], x[-1]], [y_1.T[-1, 0], y_2.T[-1, 0]], 'sk')

r_opt = bisect(residuo, 4.0, 6.0, args=(x_a, x_b, beta),
    full_output=True)
print(r_opt[1])
sol = solve_ivp(f, [x_a, x_b], [1.0, r_opt[0]],
    dense_output=True)
y = sol.sol(x)
plt.plot(x, y.T[:, 0], '-r', label=r"$r^* = 5.01665$")

plt.legend()
plt.xlabel(r"$x$")
plt.ylabel(r"$y(x)$")
plt.tight_layout()
plt.savefig("disparo.pdf")
