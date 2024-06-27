#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
import numpy as np

rng = np.random.default_rng(13)

delta = 1.5
x_0, x_1, n = -2, 3, 15
x = np.linspace(x_0, x_1, n)
y = 2.5 * x**2 - 3 * x - 2 + delta * rng.random(x.size)
z = np.polyfit(x, y, 2)
p = np.poly1d(z)
print(p)
print(f"a_0 = {p[0]:.5f}, a_1 = {p[1]:.5f}, a_2 = {p[2]:.5f}")

xp = np.linspace(x_0, x_1, 50 * n)
plt.plot(x, y, 'o')
plt.plot(xp, p(xp), '-')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.xlim([1.1 * x_0, 1.1 * x_1])
# plt.ylim([0,30])
# plt.xticks(np.linspace(0, 11, 12))
plt.tight_layout()
plt.savefig('ejem-03.pdf')
