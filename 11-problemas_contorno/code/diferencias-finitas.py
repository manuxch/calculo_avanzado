#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('../../utils/clases.mplstyle')

def p(x):
    return 0

def q(x):
    return -4

def r(x):
    return 12 * x

def solve_DF(N):
    a, b = 0, 1
    alfa , beta = 1, 3.5
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    print("x = ", x, "h = ", h)
    # Matriz A
    A = np.zeros((N-1, N-1))
    A[0, 0] = 2 + h**2 * q(x[0])
    A[0, 1] = -1 + h / 2 * p(x[0])
    A[N-2, N - 3] = -1 - h / 2 * p(x[N-1])
    A[N-2, N-2] = 2 + h**2 * q(x[N-1])
    for i in range(1, N-2):
        A[i, i - 1] = -1 - h / 2 * p(x[i])
        A[i, i] = 2 + h**2 * q(x[i])
        A[i, i + 1] = -1 + h / 2 * p(x[i])
    print(A)
    # Vector b
    b = np.zeros(N-1)
    b[0] = -h**2 * r(x[0]) + (1 + h / 2 * p(x[0])) * alfa
    b[1 : -1] = - h**2 * r(x[1 : -3])
    b[-1] = -h**2 * r(x[N-1]) + (1 - h / 2 * p(x[N-1])) * beta
    print("b = ", b)
    # Resolvemos para y
    y = np.zeros(N + 1)
    y[0] = alfa
    y[1:-1] = np.linalg.solve(A, b)
    y[-1] = beta
    return x, y

# Graficamos las soluciones
for N in [5, 10, 20, 100]:
    print(f"N = {N}")
    x, y = solve_DF(N)
    plt.plot(x, y, label=f"$N = {N}$")

plt.plot([0, 1], [1.0, 3.5], 'go')
plt.xlabel(r"$x$")
plt.ylabel(r"$y(x)$")
plt.legend(loc=4)
plt.tight_layout()
plt.savefig("dif-finitas.pdf")
