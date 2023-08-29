#!/usr/bin/env python3

import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
import numpy as np
from scipy.optimize import curve_fit

def modelo(x, a, b, c):
    return a * np.exp(-b * x) + c

rng = np.random.default_rng(13)
x_datos = np.linspace(0, 4, 50)
y = modelo(x_datos, 2.5, 1.3, 0.5)
y_ruido = 0.2 * rng.normal(size=x_datos.size)
y_datos = y + y_ruido

popt, pcov = curve_fit(modelo, x_datos, y_datos)
print(popt)

xp = np.linspace(0, 4, 200)
plt.plot(x_datos, y_datos, 'o')
plt.plot(xp, modelo(xp, *popt), '-')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.tight_layout()
plt.savefig('ejem-04.pdf')
