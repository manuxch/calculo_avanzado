#!/usr/bin/env python3

import numpy as np

a = np.array([[-2, -3], [6, 7]])
x = np.array([1, 1])

for i in range(1, 7):
    print(a @ x)
    y = np.dot(a, x)
    c = y.max()
    x = y / c
    s = f"{c:.5f} "
    s += f"[ {x[0]:.5f}, {x[1]:.5f} ]"
    print(s)

