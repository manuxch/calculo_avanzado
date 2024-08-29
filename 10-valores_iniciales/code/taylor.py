#!/usr/bin/env python3

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('../../utils/clases.mplstyle')

x = sp.Symbol('x')

x_p = np.linspace(-1, 1, 50)
y_p = np.exp(x_p)


for n in range(1, 6):
    ff = sp.series(sp.exp(x), x, x0=0, n=n)
    fo = ff.removeO()
    f_p = sp.lambdify(x, fo, 'numpy')
    print('exp(x) ~', fo)
    fig, ax = plt.subplots()
    fname = f"taylor-{n}.pdf"
    f_str = f"P_{n-1}(x) = " + sp.latex(fo)
    ax.plot(x_p, y_p, color='tab:red', label=r'$f(x) = \exp(x)$')
    if n == 1:
        ax.plot(x_p, fo * np.ones(x_p.size), color='tab:blue', label = r'$P_0(x) = 1$')
    else:
        ax.plot(x_p, f_p(x_p), color='tab:blue', label=r'$' + f_str + r'$')
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$f(x)$')
    ax.legend()
    plt.tight_layout()
    plt.savefig(fname)

