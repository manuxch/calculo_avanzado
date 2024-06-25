#!/usr/bin/env python3

import numpy as np
from numpy import linalg as la

h = np.array([[1, 1/2, 1/3], [1/2, 1/3, 1/4], [1/3, 1/4, 1/5]])
print(h)
print(f"cond(H) = {la.cond(h)}")

