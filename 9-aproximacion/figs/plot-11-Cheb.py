#!/usr/bin/env python3

import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
import numpy as np
from scipy.special import chebyt

norm = mpl.colors.Normalize(vmin=0, vmax=5)
cmap = cm.winter

T = [chebyt(n, monic=False) for n in range(6)]
x = np.linspace(-1, 1, 100)


fig, ax = plt.subplots()
n = 0
for t in T:
    print(t)
    ax.plot(x, t(x), '-', color=cmap(norm(n)), label=f"$T_{n}(x)$")
    n += 1

ax.set_xlabel(r"$x$", loc='right')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.set_xticks([-1, 1])
ax.set_yticks([-1, -0.5, 0.5, 1])
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.legend(fontsize=10, loc="center")
fig.tight_layout()
plt.savefig("fig-06.pdf")
