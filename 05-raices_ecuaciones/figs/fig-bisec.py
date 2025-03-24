#!/usr/bin/env python3

# import matplotlib
# import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('../../../utils/clases.mplstyle')

def f(x):
    return x**3 - 10 * x**2 + 5


x1, x2 = 0.0, 1.0
fig, ax = plt.subplots()
plt.axhline(color="gray")
plt.axvline(color="gray")
x = np.linspace(x1, x2, 200)
plt.plot(x, f(x), lw=3)
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.title('$f(x) = x^3 - 10 x^2 + 5$')
plt.tight_layout()
plt.savefig("bisec-ej-01.pdf")
