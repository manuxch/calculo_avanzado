#!/usr/bin/env python3

import numpy as np

Lx, Ly = 50, 50
max_iter_tiempo = 750
alpha = 5
delta_x = 1
delta_t = (delta_x ** 2)/(4 * alpha)
gamma = (alpha * delta_t) / (delta_x ** 2)

# Condiciones de borde
u_SO = 0.0
u_NO, u_SE = 50.0, 50.0
u_NE = 100.0

# Condición inicial interior
u_inicial = 50

def inicializar_u(max_iter_tiempo, ni=Lx, nj=Ly):
    # Inicializar la solución: u(k, i, j)
    u = np.full((max_iter_tiempo, ni, nj), u_inicial)
    # Establecer condiciones de borde (t, fila, columna)
    u[:, 0, :] = u_NO + np.arange(ni) * delta_x \
                * (u_NE - u_NO) / Lx
    u[:, :, 0] = u_NO - np.arange(nj) * delta_x \
                * u_NO / Ly
    u[:, -1, :] = np.arange(ni) * delta_x * u_SE / Lx
    u[:, :, -1] = u_NE - np.arange(nj) * delta_x \
                * u_SE / Ly
    return u

u = inicializar_u(max_iter_tiempo)

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({"text.usetex": True})
fig, ax = plt.subplots(figsize=(8,6))
mappable = ax.imshow(u[0], interpolation=None,
                     cmap=plt.cm.jet)
fig.colorbar(mappable, label="Temperatura (°C)", ax=ax)
ax.set_xlabel(r"$x$", fontsize=20)
ax.set_ylabel(r"$y$", fontsize=20)
fig.suptitle("Temperatura inicial")
fig.tight_layout()
fig.savefig("temp-inicial.pdf")
plt.close()

# Código que aplica el stencil en la grilla (i, j) y en cada tiempo k
def calcular(u):
    nk, ni, nj = u.shape
    for k in range(0, nk-1):
        for i in range(1, ni-1):
            for j in range(1, nj-1):
                u[k + 1, i, j] = gamma * (u[k][i+1][j] + u[k][i-1][j]
                                          + u[k][i][j+1] + u[k][i][j-1]
                                          - 4*u[k][i][j]) + u[k][i][j]
    return u

u = calcular(u)
fig, ax = plt.subplots(figsize=(8,6))
mappable = ax.imshow(u[-1], interpolation=None,
                     cmap=plt.cm.jet)
fig.colorbar(mappable, label="Temperatura (°C)", ax=ax)
ax.set_xlabel(r"$x$", fontsize=20)
ax.set_ylabel(r"$y$", fontsize=20)
fig.suptitle("Temperatura final")
fig.tight_layout()
fig.savefig("temp-final.pdf")
plt.close()

def plotheatmap(u_k, k):
    # Limpiamos la figura
    plt.clf()

    plt.title(f"Temperatura en t = {k*delta_t:.2f} u.t.")
    plt.xlabel(r"$x$", fontsize=20)
    plt.ylabel(r"$y$", fontsize=20)

    # Ploteamos u_k (u_{i,j} en `paso de tiempo k)
    plt.imshow(u_k, cmap=plt.cm.jet,
               interpolation="bicubic", vmin=0, vmax=100)
    plt.colorbar()

    return plt

import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

def animate(k):
    plotheatmap(u[k], k)

anim = animation.FuncAnimation(plt.figure(),
    animate, interval=50, frames=max_iter_tiempo,
    repeat=False)
anim.save("solucion_ecuacion_calor_t.mp4")

print("¡Hecho!")



