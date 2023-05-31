#!/usr/bin/env python3

def biseccion(f, x1, x2, switch=0, eps=1.0e-9):
    """
    raiz = biseccion(f, x1, x2, switch=0, tol=1.0e-9)
    Encuentra una raíz de f(x) = 0 por el método de
    bisección. La raíz debe estar acotada en (x1, x2).
    Haciendo switch = 1 devuelve raiz = None
    si f(x) aumenta como resultado de la bisección.
    """
    from math import log, ceil
    f1 = f(x1)
    if abs(f1) < eps: return x1
    f2 = f(x2)
    if abs(f2) < eps: return x2
    if f1 * f2 > 0:
        print("Error: la raíz no está acotada.")
        quit()
    n = ceil(log(abs(x2 - x1)/eps) / log(2.0))
    for i in range(n):
        x3 = 0.5 * (x1 + x2)
        f3 = f(x3)
        if switch and (abs(f3) > abs(f1)) \
                and (abs(f3) > abs(f2)):
            return None
        if abs(f3) < eps: return x3
        if f2 * f3 < 0.0:
            x1 = x3
            f1 = f3
        else:
            x2 = x3
            f2 = f3
    return (x1 + x2) / 2.0

def f(x):
    return x**3 - 10 * x**2 + 5

raiz = biseccion(f, 0.0, 1.0)
print(f"La raiz de f(x) = 0 es {raiz}")
