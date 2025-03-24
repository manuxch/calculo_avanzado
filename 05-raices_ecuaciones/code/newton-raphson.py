#!/usr/bin/env python3

from scipy import optimize

def NR(f, df, x, n=30, eps=1.0e-9):
    """
    raiz, iter = NR(f, df, x, n=30, tol=1.0e-9)
    Encuentra una raíz de f(x) = 0 por el método de
    Newton-Rahpson. Si se alcanza el máximo número
    de iteraciones n, devuelve None
    """
    for i in range(n):
        try:
            dx = -f(x) / df(x)
        except ZeroDivisionError:
            print("No hay convergencia.")
            quit()
        x += dx
        if abs(dx)< eps:
            return x, i
    print("Límite de iteraciones alcanzado.")
    return None, i

def f(x):
    return x**3 - 10 * x**2 + 5

def df(x):
    return 3 * x**2 - 20 * x

raiz, iteraciones = NR(f, df, 1.0)
print(f"La raiz de f(x) = 0 es {raiz}.")
print(f"Iteraciones: {iteraciones}")

raiz_2 = optimize.newton(f, 1.0, fprime=df)
print(f"La raiz 2 de f(x) = 0 es {raiz_2}.")
print(f"Diferencia: {abs(raiz_2 - raiz)}")
