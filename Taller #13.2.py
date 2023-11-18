import numpy as np

def operaciones_matriciales():
    # Obtener las dimensiones de las matrices del usuario
    filas_a = int(input("Ingrese el número de filas de la matriz A: "))
    columnas_a = int(input("Ingrese el número de columnas de la matriz A: "))
    filas_b = int(input("Ingrese el número de filas de la matriz B: "))
    columnas_b = int(input("Ingrese el número de columnas de la matriz B: "))

    # Solicitar al usuario ingresar los elementos de las matrices
    matriz_a = np.array([[float(input(f"Matriz A [{i + 1}][{j + 1}]: ")) for j in range(columnas_a)] for i in range(filas_a)])
    matriz_b = np.array([[float(input(f"Matriz B [{i + 1}][{j + 1}]: ")) for j in range(columnas_b)] for i in range(filas_b)])

    # Realizar las operaciones solicitadas
    resultado_a = 3 * matriz_a
    resultado_b = 4 * matriz_b
    resultado_suma = matriz_a + matriz_b

    try:
        resultado_producto = np.dot(matriz_b, matriz_a)
    except ValueError:
        resultado_producto = None

    # Mostrar los resultados
    print("\nResultados:")
    print("a) 3A:")
    print(resultado_a)
    print("\nb) 4B:")
    print(resultado_b)
    print("\nc) A + B:")
    print(resultado_suma)

    if resultado_producto is not None:
        print("\nd) B × A:")
        print(resultado_producto)
    else:
        print("\nLa multiplicación B × A no es posible debido a las dimensiones de las matrices.")

# Llamar a la función
operaciones_matriciales()
