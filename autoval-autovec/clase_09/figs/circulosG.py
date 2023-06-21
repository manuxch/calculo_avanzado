#!/usr/bin/env python3

# import matplotlib
# import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('../../../utils/clases.mplstyle')
fig, ax = plt.subplots()
alfa = 0.5
c1 = plt.Circle((1,0), 1.0, color='r', alpha=alfa)
c2 = plt.Circle((5,0), 2.0, color='r', alpha=alfa)
c3 = plt.Circle((9,0), 3.0, color='r', alpha=alfa)

ax.add_patch(c1)
ax.add_patch(c2)
ax.add_patch(c3)
ax.plot(1.3319, 0, '.', c='tab:blue')
ax.plot(8.811, 0, '.', c='tab:blue')
ax.plot(4.857, 0, '.', c='tab:blue')
ax.set_xlim([0, 12])
ax.set_ylim([-5, 5])
ax.set_xlabel(r'Re$(z)$')
ax.set_ylabel(r'Im$(z)$')

plt.grid()
plt.axis('equal')
plt.tight_layout()
fig.savefig('circles.pdf')
