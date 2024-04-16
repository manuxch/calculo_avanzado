#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
import numpy as np

def f(x) :
    return np.sin(np.pi * x)

x = np.linspace(0, 1, 100)
P =  np.poly1d((-4.12251, 4.12251, -0.050465))
print(P)
e = (f(x) - P(x))**2
fig, ax1 = plt.subplots()

ax1.plot(x, f(x), '-', label=r"$\sin(\pi x)$")
ax1.plot(x, P(x), '-', label=r"$P_2(x)$")
ax1.set_xlabel(r"$x$")
ax1.set_ylabel(r"$y$")


ax2 = ax1.twinx()
color = "tab:green"
ax2.plot(x, e, color=color)
ax2.set_ylabel(r"$E$", color=color)
ax2.tick_params(axis="y", labelcolor=color)


ax1.legend(loc='center')
fig.tight_layout()
plt.savefig("fig-02.pdf")
