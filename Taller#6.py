import math

eimport math

def gradosARadianes(grados):
    return grados * (math.pi / 180.0)

def calcularCosenoAproximado(x, epsilonS):
    valorEstimado = 1.0
    iteraciones = 0
    errorAbsoluto = float('inf')
    
    while errorAbsoluto >= epsilonS:
        termino = (-1) ** iteraciones * (x ** (2 * iteraciones)) / math.factorial(2 * iteraciones)
        valorEstimado += termino
        iteraciones += 1
        errorAbsoluto = abs(valorEstimado - math.cos(x))
        
    errorRelativoPorcentual = (errorAbsoluto / math.cos(x)) * 100.0
    
    return valorEstimado, errorRelativoPorcentual, iteraciones

def main():
    grados = float(input("Ingrese el valor en grados: "))
    xEnRadianes = gradosARadianes(grados)
    epsilon_s = float(input("Ingrese el criterio de error esperado (En decimales): "))
    
    valorEstimado, errorRelativoPorcentual, iteraciones = calcularCosenoAproximado(xEnRadianes, epsilon_s)
    
    print(f"Valor estimado del coseno: {valorEstimado}")
    print(f"Error relativo porcentual: {errorRelativoPorcentual:.8f}%")
    print(f"Número de iteraciones realizadas: {iteraciones}")

if __name__ == "__main__":
    main()

