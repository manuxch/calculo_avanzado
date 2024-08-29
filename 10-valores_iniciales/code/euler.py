#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('../../utils/clases.mplstyle')

def f(t, y):
    return 3 * t - y / t

def y_exacta(t):
    return t**2 + 1 / t

def euler(f, t_0, T, n, y_0):
    h = (T - t_0) / (n - 1)
    ts = t_0 + np.arange(n) * h
    ys = np.zeros(n)
    y = y_0
    for n, t in enumerate(ts):
        ys[n] = y
        y += h * f(t, y)
    return ts, ys

t_e = np.linspace(1, 6, 100)
plt.plot(t_e, y_exacta(t_e), label='Exacta')
for n in [3, 4, 5, 7, 10]:
    t, y = euler(f, 1, 6, n, 2)
    plt.plot(t, y, '.-', label=f"n = {n - 1}")

plt.xlabel(r"$t$")
plt.ylabel(r"$y(t)$")
plt.legend()
plt.tight_layout()
plt.savefig("euler.pdf")
