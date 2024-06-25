#!/usr/bin/env python3

from math import exp
import matplotlib.pyplot as plt
plt.style.use('../../utils/clases.mplstyle')
import numpy as np

x = np.array([1.00, 1.25, 1.50, 1.75, 2.00])
y = np.array([5.10, 5.79, 6.53, 7.45, 8.46])
ly = np.log(y)

for i in range(x.size):
    s = f"{i+1:2d} & "
    s += f"{x[i]:.2f} & "
    s += f"{y[i]:.2f} & "
    s += f"{ly[i]:.2f} & "
    s += f"{(x[i]**2):.2f} & "
    s += f"{(x[i]*ly[i]):.2f} & "
    print(s)

xs = x.sum()
lys = ly.sum()
x2s = (x**2).sum()
xlys = (x * ly).sum()

print(f" & {xs:.2f} & & {lys:.2f} & {x2s:.2f} & {xlys:.2f}")

xp = np.linspace(1, 2, 100)
z = np.polyfit(x, ly, 1)
p = np.poly1d(z)
print(p)
print(p[0], p[1])

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
# plt.plot(xp, p(xp), '-')
# plt.xlabel(r'$x$')
# plt.ylabel(r'$y$')
# plt.xlim([0.9,2.1])
# plt.ylim([0,9])
# plt.xticks(np.linspace(0, 11, 12))
plt.tight_layout()
plt.savefig('fig-05b.pdf')
