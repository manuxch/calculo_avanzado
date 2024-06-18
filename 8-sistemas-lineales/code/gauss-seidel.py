#!/usr/bin/env python3
import numpy as np

def gauss_seidel(A, b, w=1.0, tol=1e-10, max_iter=10000):
    n = len(b)
    x = np.zeros_like(b, dtype=np.float64)
    for it in range(max_iter):
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i, j] * x[j]

            x[i] = (1 - w) * x[i] + w * (b[i] - sigma) / A[i, i]

        if np.linalg.norm(A @ x - b, ord=np.inf) < tol:
            break

    return x, it

a = np.array([[4, -1, -6, 0],
              [-5, -4, 10, 8],
              [0, 9, 4, -2],
              [1, 0, -7, 5]])
b = np.array([2, 21, -12, -6])
x, k = gauss_seidel(a, b, w = 0.0)
residuo = np.linalg.norm(a @ x - b, ord=np.inf)
print(f"Iter: {k}, x: {x}")
print(f"Residuo: {residuo:10.6g}")
