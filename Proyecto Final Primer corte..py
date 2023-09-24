import math

def calcular_seno(x, n=10):
    seno = 0
    for i in range(n):
        coeficiente = (-1) ** i
        termino = coeficiente * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        seno += termino
    return seno

def calcular_coseno(x, n=10):
    coseno = 0
    for i in range(n):
        coeficiente = (-1) ** i
        termino = coeficiente * (x ** (2 * i)) / math.factorial(2 * i)
        coseno += termino
    return coseno

def calcular_tangente(x, n=10):
    seno = calcular_seno(x, n)
    coseno = calcular_coseno(x, n)
    tangente = seno / coseno
    return tangente

def calcular_cotangente(x, n=10):
    tangente = calcular_tangente(x, n)
    cotangente = 1 / tangente
    return cotangente

def calcular_secante(x, n=10):
    coseno = calcular_coseno(x, n)
    secante = 1 / coseno
    return secante

def calcular_cosecante(x, n=10):
    seno = calcular_seno(x, n)
    cosecante = 1 / seno
    return cosecante

while True:
    entrada = input("Ingrese una operación trigonométrica (por ejemplo, sen(1.5)): ")
    if entrada.lower() == "salir":
        break

    try:
        funcion, valor = entrada.split("(")
        valor = float(valor[:-1])  # Eliminar el paréntesis final y convertir a float

        if funcion.lower() == "sen":
            resultado = calcular_seno(valor)
        elif funcion.lower() == "cos":
            resultado = calcular_coseno(valor)
        elif funcion.lower() == "tan":
            resultado = calcular_tangente(valor)
        elif funcion.lower() == "cot":
            resultado = calcular_cotangente(valor)
        elif funcion.lower() == "sec":
            resultado = calcular_secante(valor)
        elif funcion.lower() == "csc":
            resultado = calcular_cosecante(valor)
        else:
            print("Función no válida. Las funciones válidas son: sen, cos, tan, cot, sec, csc")
            continue

        print(f"{funcion}({valor}) = {resultado:.8f}")

    except ValueError:
        print("Entrada no válida. Utilice el formato 'función(valor)' (por ejemplo, sen(1.5))")

print("Programa terminado.")