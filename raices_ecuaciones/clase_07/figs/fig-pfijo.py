#!/usr/bin/env python3

# import matplotlib
# import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('../../../utils/clases.mplstyle')

def f(x):
    return x**2 - 2


x1, x2 = -3.0, 3.0
fig, ax = plt.subplots()
plt.axhline(color="gray")
plt.axvline(color="gray")
x = np.linspace(x1, x2, 200)
plt.scatter(( -1, 2 ), ( -1, 2 ), s=48, c='tab:red', zorder=3)
plt.plot(x, f(x), lw=3, label=r"$y = x^2 - 2$")
plt.plot(x, x, lw=3, label=r"$y = x$")
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("pfijo-ej-01.pdf")
