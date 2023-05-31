#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('../../../utils/clases.mplstyle')

def coweb(f, x0, n_puntos, a=0, b=1):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    alfa = 0.5
    t = np.linspace(a, b, n_puntos)
    plt.plot(t, f(t), 'k', label=r"$y = g(x)$")
    plt.plot(t, f2(t), c='k', alpha=0.3, label=r"$ y = g_2(x)$")
    plt.plot(t, t, 'k:', label=r"$ y = x$")
    x, y = x0, f(x0)
    for _ in range(n_puntos):
        fy = f(y)
        plt.plot([x, y], [y, y], 'b', lw=1, alpha=alfa)
        plt.plot([y, y], [y, fy], 'b', lw=1, alpha=alfa)
        x, y = y, fy

    ax.set_aspect('equal')
    plt.tight_layout()
    plt.legend()
    plt.savefig("coweb.pdf")
    plt.close()

def f(x):
    r = 3.1
    return r * x * (1 - x)

def f2(x):
    r = 3.1
    return f(f(x))

coweb(f, 0.1, 100)
