#!/usr/bin/env python3

import numpy as np
from numpy import linalg as la

a = np.array([[1, 100],[0, 1]])
ai = np.array([[1, -100],[0, 1]])
a_norm = la.norm(a, ord=2)
ai_norm = la.norm(ai, ord=2)
print(f"||a|| = {a_norm}, ||ai|| = {ai_norm}")
print(f"cond(a) = {a_norm * ai_norm}")
print(f"cond(a) = {la.cond(a)}")
