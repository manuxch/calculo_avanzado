#!/usr/bin/env python3

from scipy import optimize

def f(x):
    return x**3 - 10 * x**2 + 5

raiz = optimize.bisect(f, 0.0, 1.0)
print(f"La raiz de f(x) = 0 es {raiz}")
