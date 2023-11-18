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

# Definir la matriz aumentada del sistema de ecuaciones
augmented_matrix = np.array([[1, 1, 0, 5],
                            [3, 3, 4, 23],
                            [4, 0, 1, 30]], dtype=float)

# Aplicar eliminación de Gauss-Jordan
result_matrix = gauss_jordan_elimination(augmented_matrix.copy())

# Mostrar la solución
solution = result_matrix[:, -1]
print("La solución del sistema de ecuaciones es:")
print("x1 =", solution[0])
print("x2 =", solution[1])
print("x3 =", solution[2])
