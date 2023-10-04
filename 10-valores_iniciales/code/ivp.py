#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('../../utils/clases.mplstyle')

def f(t, y):
    return 3 * t - y / t

def y_exacta(t):
    return t**2 + 1 / t

t_e = np.linspace(1, 6, 100)
plt.plot(t_e, y_exacta(t_e), label='Exacta')

from scipy.integrate import solve_ivp

sol = solve_ivp(f, [1, 6], [2], method='RK45',
    t_eval=[1, 2, 3, 4, 5, 6])

plt.plot(sol.t, sol.y[0], '.-',label="solve_ivp",
         alpha=0.7)

plt.xlabel(r"$t$")
plt.ylabel(r"$y(t)$")
plt.legend()
plt.tight_layout()
plt.savefig("solve_ivp.pdf")
