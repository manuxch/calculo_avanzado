#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../utils/clases.mplstyle')
import numpy as np

def f(x, L):
    conds = [(-L < x) & (x < -1), (-1 < x) & (x < 1), (1 < x) & (x < L)]
    vals = [0, 1, 0]
    return np.piecewise(x, conds, vals)


def plot(L, n, mas, menos, idx_fig):
    fig, ax = plt.subplots(2, 1, figsize=(8,4))
    x_L = np.linspace(-L, L, 200)
    y_L = f(x_L, L)
    ax[0].axvline(c='tab:gray')
    ax[0].axhline(c='tab:gray')
    # ax[0].plot(x_L, y_L, c='tab:blue')
    for i in range(0, mas + 1):
        print(i)
        ax[0].plot(x_L + i * 2 * L, y_L, c='tab:blue')
    for i in range(menos + 1):
        ax[0].plot(x_L - i * 2 * L, y_L, c='tab:blue')
    ax[0].set_xlabel(r"$x$")
    ax[0].set_ylabel(r"$f_L(x)$")
    ax[0].set_xlim([-10,18])

    w = np.linspace(0.01, 4 * np.pi, 100)
    n_l = np.arange(1, n + 1)
    w_n = (n_l * np.pi / L)
    a_n = np.sin(w_n) / w_n
    print(n_l)
    print(w_n)
    ax[1].axvline(c='tab:gray')
    ax[1].axhline(c='tab:gray')
    ax[1].plot(w, np.sin(w)/(w), '--')
    for p, a in zip(w_n, a_n):
        ax[1].plot([p, p], [0, a], c='tab:red')
    ax[1].set_xlabel(r"$\omega_n = n \pi / L$")
    ax[1].set_ylabel(r"$a_n$")
    plt.tight_layout()
    file_out = f"fig-01-{idx_fig}.pdf"
    plt.savefig(file_out)


plot(2, 8, 4, 2, 1)
plot(4, 16, 2, 1, 2)
plot(8, 32, 1, 0, 3)
