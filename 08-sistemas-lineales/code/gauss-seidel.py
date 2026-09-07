#!/usr/bin/env python3
import numpy as np

def gauss_seidel(A, b, w=1.0, tol=1e-10, max_iter=10000):
    n = len(b)
    x = np.ones_like(b, dtype=np.float64)
    for it in range(max_iter):
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    suma += A[i, j] * x[j]

            x[i] = (w / A[i,i]) * (b[i] - suma) \
                    + (1 - w) * x[i]

        # print(it, x, suma, np.dot(A, x), b)
        if np.linalg.norm(A @ x - b) < tol:
            break

    return x, it

a = np.array([[4, -1, -6, 0],
              [0, 9, 4, -2],
              [5, -4, 10, 8],
              [1, 0, -3, 5]])
b = np.array([12, -2, -11, 28])
x, k = gauss_seidel(a, b, w = 0.8, max_iter=10000)
residuo = np.linalg.norm(a @ x - b, ord=np.inf)
print(f"Iteración: {k}, x: {x}")
print(f"Residuo: {residuo:10.6g}")
