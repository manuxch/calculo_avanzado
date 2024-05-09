#!/usr/bin/env python3
import numpy as np

def iter_potencia(A, num_iteraciones):
    n = A.shape[0]
    # Inicializar un vector unitario de tamaño n
    x = np.ones(n)

    for _ in range(num_iteraciones):
        # Multiplicar la matriz A por el vector x
        y = np.dot(A, x)
        # Obtener la norma máxima
        yy = np.abs(y)
        c = yy.max()
        print(c)
        # Normalizar el vector resultante
        x = y / c

    # Devolver el autovalor dominante y el autovector
    # correspondiente
    return c, x

# Ejemplo de uso
# Definir una matriz de ejemplo
A = np.array([[0, 11, -5],
              [-2, 17, -7],
              [-4, 26, -10]])

# Especificar el número de iteraciones
num_iteraciones = 100

# Aplicar el algoritmo de las potencias
autovalor, autovector = iter_potencia(A, num_iteraciones)

print(f"Autovalor dominante: {autovalor}")
print("Autovector correspondiente:")
print(autovector)
