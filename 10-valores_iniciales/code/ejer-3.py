#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('../../utils/clases.mplstyle')

def f(t, y):
    return y * (1 - y)


def euler(f, t_0, T, n, y_0):
    h = (T - t_0) / (n)
    ts = t_0 + np.arange(n + 1) * h
    print(ts)
    ys = np.zeros(n+ 1)
    y = y_0
    for n, t in enumerate(ts):
        ys[n] = y
        y += h * f(t, y)
    return ts, ys

for n in [4, 16, 32]:
    t, y = euler(f, 0, 1, n, 0.5)
    plt.plot(t, y, '.-', label=f"n = {n}")
    print("tn", t[-1])
    print("yn", y[-1])

plt.xlabel(r"$t$")
plt.ylabel(r"$y(t)$")
plt.legend()
plt.tight_layout()
plt.show()

