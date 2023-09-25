import math

def aproximacion_expansion(x, n):
    resultado = 1.0
    error_anterior = 0.0
    
    for i in range(1, n + 1):
        termino = (x ** i) / math.factorial(i)
        resultado += termino
        epsilon = abs((resultado - error_anterior) / resultado) * 100
        print(f"Iteración {i}: {resultado:.8f}, εa = {epsilon:.8f}%")
        if epsilon < 0.000001:  
            break
        error_anterior = resultado
    
    return resultado

x = -0.75
n = 100  
resultado = aproximacion_expansion(x, n)
print(f"Resultado final: {resultado:.8f}")
