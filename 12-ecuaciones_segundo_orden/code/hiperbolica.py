#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Parámetros
L, T = 1.0, 1.0    # Dominio
Nx, Nt = 100, 1000 # Grilla
c = 1.0            # Velocidad
# Discretización
h, k = L / (Nx - 1), T / (Nt - 1)
l2 = (c * k / h)**2  # lambda**2
x = np.linspace(0, L, Nx)
t = np.linspace(0, T, Nt)

# Inicialización
u = np.zeros((Nt, Nx))
u[0, :] = np.sin(np.pi * x)  # Condición inicial
u[1, 1:Nx-1] = u[0, 1:Nx-1] + 0.5 * l2 * (u[0, 2:Nx] \
    - 2 * u[0, 1:Nx-1] + u[0, 0:Nx-2])

# Iteración en el tiempo
for n in range(1, Nt - 1):
    for i in range(1, Nx - 1):
        u[n + 1, i] = 2 * (1 - l2) * u[n, i] \
            - u[n - 1, i] + l2 * (u[n, i + 1] \
            + u[n, i - 1])

#Visualización de la solución
plt.imshow(u, extent=[0, L, 0, T], origin='lower',
           aspect='auto', cmap='seismic')
plt.colorbar()
plt.xlabel('Posición (x)')
plt.ylabel('Tiempo (t)')
plt.savefig('onda-1.pdf')
# plt.show()

# def plotheatmap(x, u, k):
    # # Limpiamos la figura
    # plt.clf()
    # plt.xlabel(r"$x$", fontsize=20)
    # plt.ylabel(r"$y$", fontsize=20)
    # # Ploteamos u_k (u_{i,j} en `paso de tiempo k)
    # plt.xlim([0, 1])
    # plt.ylim([-1, 1])
    # plt.plot(x, u[k, :])
    # return plt

# import matplotlib.animation as animation
# from matplotlib.animation import FuncAnimation

# def animate(k):
    # plotheatmap(x, u, k)

# anim = animation.FuncAnimation(plt.figure(),
    # animate, interval=5, frames=Nt, repeat=False)
# anim.save("solucion_ecuacion_onda-2.mp4")

# print("¡Hecho!")

