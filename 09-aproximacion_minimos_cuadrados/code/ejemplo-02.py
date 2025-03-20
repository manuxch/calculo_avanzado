#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
from math import exp
import numpy as np

x = np.array([1.00, 1.25, 1.50, 1.75, 2.00])
y = np.array([5.10, 5.79, 6.53, 7.45, 8.46])
ly = np.log(y)

z = np.polyfit(x, ly, 1)
p = np.poly1d(z)
print(p)
print(f"ln(b) = {p[0]:.5f}, a = {p[1]:.5f}")

xp = np.linspace(1, 2, 100)
ye = exp(p[0]) * np.exp(p[1] * xp)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x, y, 'o')
ax1.plot(xp, ye)
ax2.plot(x, ly, 'o')
ax2.plot(xp, p(xp))
ax1.set_ylim([4, 9])
ax2.set_ylim([1.5, 2.5])
ax1.set_xlabel(r"$x$")
ax2.set_xlabel(r"$x$")
ax1.set_ylabel(r"$y$")
ax2.set_ylabel(r"$\ln y$")
plt.tight_layout()
plt.savefig('ejem-02.pdf')
