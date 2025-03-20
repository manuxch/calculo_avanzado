#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('../../utils/clases.mplstyle')

# Definir los vectores v1 y v2
x1 = np.array([3, 1])
x2 = np.array([2, 2])

# Definir los vectores u1 y u2
v1 = np.array([ 3, 1])
v2 = np.array([-2/5, 6/5])

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Graficar los vectores
ax.quiver(0, 0, x1[0], x1[1], angles='xy', scale_units='xy', scale=1, color='tab:blue')
ax.annotate(r'$\vec{x}_1 = \vec{v}_1$', xy=(x1[0], x1[1]), fontsize=22)
ax.quiver(0, 0, x2[0], x2[1], angles='xy', scale_units='xy', scale=1, color='tab:orange')
ax.annotate(r'$\vec{x}_2$', xy=(x2[0], x2[1]), fontsize=22)
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='tab:red')
ax.annotate(r'$\vec{v}_2$', xy=(v2[0], v2[1]), fontsize=22)

# Configurar los límites de los ejes
ax.set_xlim([-0.5, 4])
ax.set_ylim([-0.5, 2.5])
ax.set_aspect('equal')

# Etiquetas y leyenda
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')

# Mostrar el gráfico
plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.tight_layout()
plt.savefig("gram-schmidt.pdf")

