#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
plt.style.use('../../utils/clases.mplstyle')

def LV(t, z, a, b, d, g):
    x, y = z
    return [a * x - b * x * y, d * x * y - g * y]

sol = solve_ivp(LV, [0, 15], [10, 5],
    args=(1.5, 1, 1, 3), dense_output=True)

t = np.linspace(0, 15, 300)
z = sol.sol(t)
plt.plot(t, z.T[:,0], label=r'$x$')
plt.plot(t, z.T[:,1], label=r'$y$')
plt.xlabel(r"$t$")
plt.legend()
plt.tight_layout()
plt.savefig("lv.pdf")
