import numpy as np

def gauss_jordan_elimination(matrix):
    # Aplicar eliminación hacia adelante
    for i in range(len(matrix)):
        # Pivote actual
        pivot = matrix[i][i]

        # Dividir la fila actual por el pivote para hacer el pivote 1
        matrix[i] = matrix[i] / pivot

        # Eliminación hacia adelante para hacer ceros en las otras filas
        for j in range(len(matrix)):
            if i != j:
                factor = matrix[j][i]
                matrix[j] -= factor * matrix[i]

    return matrix

def find_inverse(matrix):
    # Obtener el tamaño de la matriz
    n = len(matrix)

    # Crear una matriz aumentada [A | I] para aplicar Gauss-Jordan
    augmented_matrix = np.hstack((matrix, np.identity(n)))

    # Aplicar eliminación de Gauss-Jordan a la matriz aumentada
    result_matrix = gauss_jordan_elimination(augmented_matrix.copy())

    # Extraer la matriz inversa de la parte derecha de la matriz aumentada
    inverse_matrix = result_matrix[:, n:]

    return inverse_matrix

# Definir la matriz A
matrix_A = np.array([[3, 2, 2],
                    [3, 1, -3],
                    [1, 0, -2]], dtype=float)

# Definir la matriz B
matrix_B = np.array([[1, 2, 0],
                    [2, 0, -1],
                    [1, 0, 1],
                    [4, -1, 1],
                    [4, -2, 0]], dtype=float)

# Encontrar las inversas
inverse_A = find_inverse(matrix_A)
inverse_B = find_inverse(matrix_B)

# Mostrar las inversas
print("Inversa de la matriz A:")
print(inverse_A)

print("\nInversa de la matriz B:")
print(inverse_B)
