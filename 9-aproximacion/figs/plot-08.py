#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../utils/clases.mplstyle')
import numpy as np

def f(x) :
    return 1 / np.sqrt(1 - x**2)

x = np.linspace(-1, 1, 100)
y = f(x)


fig, ax = plt.subplots()

ax.plot(x, f(x), '-', label=r"$w(x)$")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$w(x)$")

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticks([1, 2, 3, 4, 5])
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
ax.set_ylim([0, 5])
ax.axvline(x=-1, color='tab:grey')
ax.axvline(x=1, color='tab:grey')


fig.tight_layout()
plt.savefig("fig-08.pdf")
