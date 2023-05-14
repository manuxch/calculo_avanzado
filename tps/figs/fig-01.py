#!/usr/bin/env python3

# import matplotlib
# import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('../../utils/clases.mplstyle')

def f(x):
    return np.piecewise(x, [x < 0, (x > 0) & (x < 2), x > 2 ],
                        [lambda x: x + 1, 1, lambda x: 3 - x])


fig, ax = plt.subplots(figsize=(8,4))
plt.axhline(color="gray")
plt.axvline(color="gray")
x = np.linspace(-1, 3, 200)
tau = [0, 1, 2]
for t in tau:
    plt.plot(x + t * 4, f(x), c='tab:blue', lw=3)
plt.xlabel('$x$')
ax.set_xticks([2, 3, 4, 6, 7, 8, 14, 15, 16])
ax.set_yticks([0, 1])
plt.ylabel('$f(x)$')
plt.xlim([0, 9])
plt.ylim([0, 1.1])
plt.tight_layout()
plt.savefig("fig-01.pdf")



