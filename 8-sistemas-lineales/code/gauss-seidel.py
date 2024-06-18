#!/usr/bin/env python3
import numpy as np
def gauss_seidel(A, b, tolerance=1e-10, max_iterations=10000):

    x = np.zeros_like(b, dtype=np.double)

    #Iterate
    for k in range(max_iterations):
        x_old  = x.copy()
        #Loop over rows
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) / A[i ,i]

        #Stop condition
        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
            break

    return x, k

a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])
x, k = gauss_seidel(a, b)
print(x, k)
print(a @ x - b)

