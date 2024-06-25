#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../utils/clases.mplstyle')
import numpy as np

x = np.array([0, 0.25, 0.50, 0.75, 1.00])
y = np.array([1.0, 1.284, 1.6487, 2.117, 2.7183])

xp = np.linspace(0, 1, 100)
z = np.polyfit(x, y, 2)
p = np.poly1d(z)
print(p)


plt.plot(x, y, 'o')
plt.plot(xp, p(xp), '-')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.xlim([-0.1,1.1])
plt.ylim([0,3])
# plt.xticks(np.linspace(0, 11, 12))
plt.tight_layout()
plt.savefig('fig-04.pdf')
