#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../utils/clases.mplstyle')
import numpy as np

rng = np.random.default_rng(14)

delta = 5.5
x = np.linspace(1, 10, 10).astype(int)
xp = np.linspace(0, 11, 100)
y = 2.5 * x + delta * rng.random(x.size)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
print(p)

for i in range(x.size):
    s = f"{x[i]:2d} & "
    s += f"{y[i]:.2f} & "
    s += f"{x[i]**2:2d} & "
    s += f"{x[i]*y[i]:.2f} & "
    s += f"{p(x[i]):.2f} \\\\ "
    print(s)

a = x.sum()
b = y.sum()
c = (x*x).sum()
d = (x*y).sum()
f = ((y - p(x))**2).sum()
print(f"{a:2d} & {b:.2f} & {c:2d} & {d:.2f} & {f:.2f} \\\\")

plt.plot(x, y, 'o')
plt.plot(xp, p(xp), '-')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.xlim([0,9])
plt.ylim([0,30])
plt.xticks(np.linspace(0, 11, 12))
plt.tight_layout()
plt.savefig('fig-03.pdf')
