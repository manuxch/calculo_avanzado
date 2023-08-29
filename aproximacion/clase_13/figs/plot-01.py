#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
import numpy as np

rng = np.random.default_rng(14)

delta = 5.5
x = np.linspace(1, 10, 10).astype(int)
y = 2.5 * x + delta * rng.random(x.size)
print(x)
print(y)

for i in range(5):
    print(f"{x[i]:2d} & {y[i]:.2f} & {x[i+5]:2d} & {y[i+5]:.2f} \\\\")

plt.plot(x, y, 'o')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.xlim([0,9])
plt.ylim([0,30])
plt.xticks(np.linspace(0, 11, 12))
plt.tight_layout()
plt.savefig('fig-01.pdf')
