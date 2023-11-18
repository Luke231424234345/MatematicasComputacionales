def producto_escalar():
    # Obtener la longitud de los vectores del usuario
    n = int(input("Ingrese la longitud de los vectores: "))

    # Inicializar los vectores con ceros
    vector_a = [0] * n
    vector_b = [0] * n

    # Solicitar al usuario ingresar los elementos de los vectores
    print("Ingrese los elementos del primer vector:")
    for i in range(n):
        vector_a[i] = float(input(f"Elemento {i + 1}: "))

    print("Ingrese los elementos del segundo vector:")
    for i in range(n):
        vector_b[i] = float(input(f"Elemento {i + 1}: "))

    # Calcular el producto escalar
    producto = sum(a * b for a, b in zip(vector_a, vector_b))

    # Mostrar el resultado
    print(f"El producto escalar de los vectores es: {producto}")

# Llamar a la función
producto_escalar()
