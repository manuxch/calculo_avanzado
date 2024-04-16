#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

# Parámetros del problema
L = 1.0  # Longitud del dominio
T = 0.5   # Tiempo total
Nx = 11  # Número de puntos en el espacio
Nt = 50  # Número de pasos de tiempo
alpha = 1.0  # Difusividad térmica

# Tamaño de paso en el espacio y el tiempo
dx = L / (Nx - 1)
dt = T / Nt

# Condiciones iniciales y de contorno
def initial_condition(x):
    return np.sin(np.pi * x / L)

def boundary_conditions(t):
    return 0.0

# Inicialización del arreglo de temperatura
u = np.zeros(Nx)

# Inicialización de la matriz tridiagonal
# A = np.zeros((Nx, Nx))
# r = alpha * dt / (2 * dx**2)

# Construcción de la matriz tridiagonal
# for i in range(1, Nx - 1):
# A[i, i - 1] = -r
# A[i, i] = 1 + 2 * r
# A[i, i + 1] = -r
r = alpha * dt / (2 * dx**2)
diagonals = [1 + r, -2 * r, 1 + r]
A = diags(diagonals, [-1, 0, 1], shape=(Nx, Nx)).tocsc()
u = initial_condition(np.arange(0, 1, Nx))
print(A.todense())
print(u)

# Bucle temporal
for n in range(Nt):
    # Aplicar condiciones de contorno
    u[0] = boundary_conditions(n * dt)
    u[Nx - 1] = boundary_conditions(n * dt)

    # Resolver el sistema tridiagonal
    b = u.copy()
    # u = np.linalg.solve(A, b)
    u = spsolve(A, u)

# Gráfica de la solución
x = np.linspace(0, L, Nx)
plt.plot(x, u)
plt.xlabel('Posición')
plt.ylabel('Temperatura')
plt.title('Evolución de la Temperatura en 1D')
plt.show()

