#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
import numpy as np
import sympy as sym
from sympy.abc import x, n
import sympy.printing as prt

def min_Legendre(f, L):
    c = []
    for l in L:
        fl = sym.integrate(l * f, (x, -1, 1))
        alfa = sym.integrate(l * l, (x, -1, 1))
        c.append(fl / alfa)
    return c

f = sym.exp(-x) - (x-1/2)**2
f_num = sym.lambdify([x], f, modules='numpy')
x_points = np.linspace(-1, 1, 100)
plt.plot(x_points, f_num(x_points),
    label=r'$f(x)=e^{-x} - (x-1/2)^2$', alpha=0.5)

for n in range(1, 5):
    print(f"n = {n}")
    L = [sym.legendre(n, x) for n in range(n)]
    c = min_Legendre(f, L)
    P = sum(c[i] * L[i] for i in range(len(L)))
    lbl = f"$P_{n-1} = {prt.latex(sym.N(sym.collect(P, x), 3))}$"
    print(lbl)
    if n == 1:
        y_approx = P * np.ones(x_points.size)
    else:
        Pn = sym.lambdify([x], P, modules='numpy')
        y_approx = Pn(x_points)
    plt.plot(x_points, y_approx, label=lbl, alpha=0.7)

plt.legend(fontsize=10)
plt.xlabel('$x$')
plt.tight_layout()
plt.savefig("fig-05.pdf")
