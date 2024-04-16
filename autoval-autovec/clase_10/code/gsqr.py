#!/usr/bin/env python3

import numpy as np

def gram_schmidt_qr(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]

    return Q, R

# Ejemplo de uso
# Definir una matriz de ejemplo
A = np.array([[1, 4, 3],
              [2, 5, 1],
              [3, 6, 2]])

# Aplicar la factorización QR usando el método
# de Gram-Schmidt
Q, R = gram_schmidt_qr(A)

print("Matriz Q:")
print(Q)
print("Matriz R:")
print(R)
