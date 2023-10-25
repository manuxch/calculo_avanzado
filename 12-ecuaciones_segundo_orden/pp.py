#!/usr/bin/env python3
import numpy as np


def m2i(i, j, m):
    return j * (m + 1) + i
    # return i + m * (j-1)

# n = 2
# m = 2
# for j in range(m + 1):
    # for i in range(n + 1):
        # l = m2i(i, j, n)
        # print(i,j, l)

n, m = 4, 4
# m2v = lambda i, j: j * n + i
m2v = lambda i, j: j * (n + 1) + i - 5
Lx, Ly = 0.5, 0.5
x = np.linspace(0, Lx, n + 1)
y = np.linspace(0, Ly, m + 1)
h = x[1] - x[0]
k = y[1] - y[0]
print(h, k)
u = np.zeros((n + 1, m + 1))
Ix = range(0, n + 1)
Iy = range(0, m + 1)
u[:, 0] = 0
u[0, :] = 0
u[-1, :] = y * 200
u[:, -1] = x * 200
N = (n-1)*(m-1)
A = np.zeros((N - 1, N - 1))
b = np.zeros(N - 1)
for i in Ix[1 : -1]:
    for j in Ix[1 : -1]:
        p = m2v(i, j)
        print(i, j, p)
        A[p, p] = 4

print(u)
# N = (n - 1) * (m - 1)
# A = np.zeros((N, N))
# b = np.zeros(N)

# for j in Iy[1:-1]:
    # i = 0
    # p = m2i(i, j, n)
    # A[p, p] = 4
    # for i in Ix[1:-1]:
        # p = m2v(i, j)
        # print(i, j, p)
        # A[p, m2v(i, j-1)] = -1
        # A[p, m2v(i-1, j)] = -1
        # A[p, p] = 4
        # A[p, m2v(i+1, j)] = -1
        # A[p, m2v(i, j+1)] = -1

    # i = n
    # p = m2i(i, j, n)
    # A[p, P] = 4

# print(A)


# A = np.array([[4, -1, 0, -1, 0, 0, 0, 0, 0],
             # [-1, 4, -1, 0, -1, 0, 0, 0, 0],
             # [0, -1, 4, 0, 0, -1, 0, 0, 0],
             # [-1, 0, 0, 4, -1, 0, -1, 0, 0],
             # [0, -1, 0, -1, 4, -1, 0, -1, 0],
              # [0, 0, -1, 0, -1, 4, 0, 0, -1],
              # [0, 0, 0, -1, 0, 0, 4, -1, 0],
              # [0, 0, 0, 0, -1, 0, -1, 4, -1],
              # [0, 0, 0, 0, 0, -1, 0, -1, 4]])

# b = np.array([0, 0, 25, 0, 0, 50, 25, 50, 150])
# u = np.linalg.solve(A, b)
# print(u)
