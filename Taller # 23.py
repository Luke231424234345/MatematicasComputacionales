def lagrange_interpolation(x_values, y_values):
    """
    Encuentra el polinomio de interpolación de Lagrange para un conjunto de puntos.

    Parameters:
    - x_values: Lista de valores x.
    - y_values: Lista de valores y correspondientes.

    Returns:
    - polynomial: Polinomio de interpolación de Lagrange en formato de cadena.
    """
    polynomial = ""
    n = len(x_values)

    for i in range(n):
        term = str(y_values[i])
        for j in range(n):
            if j != i:
                term += f" * (x - {x_values[j]}) / ({x_values[i]} - {x_values[j]})"
        if i != n - 1:
            term += " + "
        polynomial += term

    return polynomial

# Ejemplo de puntos
x_values = [0, 1, 2, 3, 4]
y_values = [1, 0.9, -1, -2.3, 1.8]

# Encontrar el polinomio de interpolación de Lagrange
polynomial = lagrange_interpolation(x_values, y_values)

# Imprimir el polinomio
print(f"Polinomio de Interpolación de Lagrange: P(x) = {polynomial}")
