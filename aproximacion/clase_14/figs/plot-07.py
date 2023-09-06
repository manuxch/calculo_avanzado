#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
import numpy as np
import sympy as sym
from sympy.abc import x, n
import sympy.printing as prt

def min_Chebyshev(f, T):
    c = []
    for t in T:
        ft = sym.integrate(t * f / (sym.sqrt(1 - x**2)), (x, -1, 1))
        alfa = sym.integrate(t * t / (sym.sqrt(1 - x**2)), (x, -1, 1))
        c.append(ft / alfa)
    return c

f = x**5 - 4 * x**4 + x**3 - x - 3
f_num = sym.lambdify([x], f, modules='numpy')

fig, (ax1, ax2) = plt.subplots(2,1, figsize=(4, 6), sharex=True)
x_points = np.linspace(-1, 1, 100)
ax1.plot(x_points, f_num(x_points),
    label=r'$f(x)=x^5 - 4 x^4 + x^3 - x - 3$', alpha=0.5)

for n in range(1, 6):
    print(f"n = {n - 1}")
    T = [sym.chebyshevt(n, x) for n in range(n)]
    c = min_Chebyshev(f, T)
    P = sum(c[i] * T[i] for i in range(len(T)))
    lbl = f"$P_{n-1} = {prt.latex(sym.N(sym.collect(P, x), 3))}$"
    print(lbl)
    if n == 1:
        y_approx = P * np.ones(x_points.size)
    else:
        Pn = sym.lambdify([x], P, modules='numpy')
        y_approx = Pn(x_points)
        if n > 2:
            ax2.plot(x_points, (f_num(x_points) - y_approx)**2,
                     label=f"$E_{n-1}^2$", alpha=0.7)
    ax1.plot(x_points, y_approx, label=lbl, alpha=0.7)

ax1.legend(fontsize=8)
ax2.legend(fontsize=8)
plt.xlabel('$x$', fontsize=16)
plt.xticks(fontsize=12)
ax1.tick_params(axis='both', which='major', labelsize=10)
ax2.tick_params(axis='both', which='major', labelsize=10)
plt.tight_layout()
plt.savefig("fig-07.pdf")
