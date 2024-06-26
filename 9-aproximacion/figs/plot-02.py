#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../utils/clases.mplstyle')
import numpy as np

rng = np.random.default_rng(14)

delta = 5.5
x = np.linspace(1, 10, 10)
xp = np.linspace(0, 11, 100)
y = 2.5 * x + delta * rng.random(x.size)
z = np.polyfit(x, y, 9)
p = np.poly1d(z)
print(p)

plt.plot(x, y, 'o')
plt.plot(xp, p(xp), '-')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.xlim([0,9])
plt.ylim([0,30])
plt.xticks(np.linspace(0, 11, 12))
plt.tight_layout()
plt.savefig('fig-02.pdf')
