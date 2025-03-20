#!/usr/bin/env python3

import numpy as np
from scipy import linalg

a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])
x = linalg.solve(a, b)
print('x = ', x)

# Verificación
print('a @ x ?', (np.dot(a, x) == b))
print('a @ x ?', np.allclose(a @ x, b))
print('a @ x =', a @ x)
# Descomposición LU
p, l, u = linalg.lu(a)
print(p)
print(l)
print(u)
