import math

def calcular_valor_taylor(x, n):
    valor_aproximado = 0
    for i in range(n + 1):
        valor_aproximado += (-x) ** i / math.factorial(i)
    return valor_aproximado

x_base = 0.5


x_estimado = 0.505


valor_verdadero = math.exp(-x_estimado)


for n in range(16):
    valor_aproximado = calcular_valor_taylor(x_estimado - x_base, n)
    error_relativo_porcentual = abs((valor_verdadero - valor_aproximado) / valor_verdadero) * 100
    print(f"Orden {n}: Valor Aproximado = {valor_aproximado}, Error Relativo Porcentual = {error_relativo_porcentual}%")
