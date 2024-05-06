#!/usr/bin/env python3
import numpy as np

def iter_potencia(A, num_iteraciones):
    n = A.shape[0]
    # Inicializar un vector aleatorio de tamaño n
    b = np.random.rand(n)
    # Normalizar el vector
    b = b / np.linalg.norm(b)

    for _ in range(num_iteraciones):
        # Multiplicar la matriz A por el vector b
        Ab = np.dot(A, b)
        # Calcular el autovalor dominante
        autovalor = np.dot(b, Ab)
        # Normalizar el vector resultante
        b = Ab / np.linalg.norm(Ab)

    # Devolver el autovalor dominante y el autovector
    # correspondiente
    return autovalor, b

# Ejemplo de uso
# Definir una matriz de ejemplo

A = np.array([[2, 0, 0],
              [1, 1, 2],
              [1, -1, 4]])

# Especificar el número de iteraciones
num_iteraciones = 100

# Aplicar el algoritmo de las potencias
autovalor, autovector = iter_potencia(A, num_iteraciones)

print(f"Autovalor dominante: {autovalor}")
print("Autovector correspondiente:")
print(autovector)
