#!/usr/bin/env python3

import math
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({"text.usetex": True})
fig, ax = plt.subplots(figsize=(8,6))
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

def sol_exacta(x, t):
    u = math.exp(-np.pi**2 * t) * np.sin(np.pi * x)
    return u

def solve_matricial(u, h, k, alfa):
    lamb = alfa**2 * k / h**2
    n = u.shape[0]
    print(f"{alfa=} {h=} {k=} {lamb=} {n=}")
    diagonals_A = [-lamb/2, 1 + lamb, -lamb/2]
    A = diags(diagonals_A, [-1, 0, 1], shape=(n, n)).tocsc()
    diagonals_B = [lamb/2, 1 - lamb, lamb/2]
    B = diags(diagonals_B, [-1, 0, 1], shape=(n, n)).tocsc()
    n_t = int(0.5 / k)
    # print(A.todense())
    # print(B.todense())
    # print(u)
    for i in range(n_t):
        u = spsolve(A, B @ u)
        u[0] = u[-1] = 0.0
    return u

n = 10
h = 0.1
k = 0.01
alfa = 1.0
x = np.arange(n + 1) * h
u_0 = np.sin(np.pi * x)
u_0[0] = u_0[-1] = 0.0
u = solve_matricial(u_0, h, k, alfa)
u_ex = sol_exacta(x, 0.5)
for i in range(x.size):
    print(f"{i:1d} & {x[i]:.1f} & {u[i]:.5f} & {u_ex[i]:.5f} & {abs(u[i] - u_ex[i]):.3e} \\\\")

plt.plot(x, u, label=r"$u(t = 0.5)$")
plt.plot(x, u_ex, label=r"$u_e(t = 0.5)$")
plt.xlabel(r"$x$")
plt.ylabel(r"$T(x)$")
plt.legend()
plt.tight_layout()
plt.show()


