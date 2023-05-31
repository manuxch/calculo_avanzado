#!/usr/bin/env python3

from scipy import optimize

def f(x):
    return x**3 - 10 * x**2 + 5

def df(x):
    return 3 * x**2 - 20 * x

metodos = ['bisect', 'newton', 'brentq', 'toms748']

for m in metodos:
    sol = optimize.root_scalar(f, x0=1.0,
            bracket=[0.01, 2], fprime=df, method=m)
    print(f"Método: {m:7s}, raiz = {sol.root}")
