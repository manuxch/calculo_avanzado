#!/usr/bin/env python3

import numpy as np

def f(x):
    return 4 * x * (1 - x)

n_x, n_t = 101, 50
Lx = 1
h = Lx / n_x
k = 0.001
alfa = 1
C = alfa * k / h # Número de Courant
print(C)
C2 = C**2

u = np.full((n_t, n_x), 0.0)

# Condición inicial
x = np.linspace(0, 1, n_x)
u[0, :] = f(x)
print(u[0, :])

# Primer paso temporal:
u[1, 1:-1] = (1 - C2) * f(x[1:-1]) * C2/2 * f(x[2:]) + C2/2 * f(x[:-2])
u[1, 0] = u[1, -1] = 0
print(u[1,:])

for j in range(1, n_t - 1):
    u[j+1, 1:-1] = 2*(1-C2) * u[j, 1:-1] + C2*(u[j, 2:] + u[j, :-2]) - u[j-1, 1:-1]
    u[j+1, 0] = u[j+1, -1] = 0.0

print(u[-1:])

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({"text.usetex": True})
fig, ax = plt.subplots(figsize=(8,6))

def plotheatmap(x, u_k, j):
    # Limpiamos la figura
    plt.clf()

    plt.title(f"Onda en t = {j*k:.2f} u.t.")
    plt.xlabel(r"$x$", fontsize=20)
    plt.ylabel(r"$u(x, t)$", fontsize=20)
    plt.plot(x, u_k[j, :])
    return plt

import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

def animate(k):
    plotheatmap(x, u, k)

anim = animation.FuncAnimation(plt.figure(),
    animate, interval=50, frames=n_t, repeat=False)
anim.save("solucion_ecuacion_onda.mp4")

print("¡Hecho!")
