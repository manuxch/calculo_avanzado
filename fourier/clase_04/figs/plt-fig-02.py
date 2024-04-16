#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
import numpy as np

def f(x):
    conds = [np.abs(x) < 1, np.abs(x) > 1]
    vals = [1, 0]
    return np.piecewise(x, conds, vals)

def intf(x, a):
    ret = np.zeros(x.size)
    omega = np.linspace(0.001, a, x.size)
    do = omega[1] - omega[0]
    for i, val in enumerate(x):
        ret[i] = np.trapz(np.cos(val * omega) * np.sin(omega) / omega, dx=do)
    return 2 / np.pi * ret

x_n = np.linspace(-3, 3, 500)

for a in [8, 16, 32, 512]:
    y_n = intf(x_n, a)
    plt.axvline(c='tab:gray')
    plt.axhline(c='tab:gray')
    lab = f"$a = {{{str(a)}}}$"
    plt.plot(x_n, y_n, label=lab, alpha=0.75)
plt.xlabel(r"$x$")
plt.ylabel(r"$f_a(x)$")
plt.legend()
plt.tight_layout()
plt.savefig("fig-02.pdf")
