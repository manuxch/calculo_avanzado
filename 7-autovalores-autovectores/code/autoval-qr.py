#!/usr/bin/env python3
import numpy as np

def algoritmo_qr(A, num_iter):
    n = A.shape[0]
    autovalores = np.zeros(n, dtype=np.complex128)
    for i in range(num_iter):
        Q, R = np.linalg.qr(A)
        A = np.dot(R, Q)
    for i in range(n):
        autovalores[i] = A[i, i]
    return autovalores

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

num_iter = 100
autovalores = algoritmo_qr(A, num_iter)
print("Autovalores:")
print(autovalores)
