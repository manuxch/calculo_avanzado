#!/usr/bin/env python3

def punto_fijo(g, x0, max_n=200, eps=1.0e-5):
    """
    p = punto_fijo(g, x0, max_n=200, eps=1.0e-5)
    Itera la relación x = g(x0), x0 <- x
    hasta agotar el número de iteraciones (en ese
    caso devuelve None), o hasta que se produzca
    convergencia con la tolerancia eps, en la que
    devuelve el punto fijo.
    """
    for k in range(max_n):
        x = g(x0)
        delta_x = x - x0
        print(f"{k:3d} {x:1.16f} {delta_x:1.16f}")
        if abs(delta_x / x) < eps:
            break
        x0 = x
    else:
        x = None
    return x

def g(x):
    """
    Mapeo logístico x_{n+1} = r x_n (1 - x_n)
    """
    r = 2.9  # Un punto fijo
    # r = 3.1  # Atractor de dos puntos
    # r = 4.0  # Región caótica
    return r * x * (1 - x)

pfijo = punto_fijo(g, 0.1)
print(f"El punto fijo de g(p) = p es {pfijo}")
