#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# Definir los vectores v1 y v2
v1 = np.array([2, 1])
v2 = np.array([-1, 3])

# Definir los vectores u1 y u2
u1 = np.array([2/np.sqrt(5), 1/np.sqrt(5)])
u2 = np.array([-2/np.sqrt(5), 3/np.sqrt(5)])

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Graficar los vectores
ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='tab:blue', label='u1')
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='tab:blue', label='u2')
ax.quiver(0, 0, u1[0], u1[1], angles='xy', scale_units='xy', scale=1, color='tab:red', label='u1')
ax.quiver(0, 0, u2[0], u2[1], angles='xy', scale_units='xy', scale=1, color='tab:red', label='u2')

# Configurar los límites de los ejes
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_aspect('equal')

# Etiquetas y leyenda
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()

# Mostrar el gráfico
plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.savefig("gram-schmidt.pdf")

