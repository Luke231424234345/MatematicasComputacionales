import math
def calcular_valor_taylor(x, orden):
    valor_aproximado = 0
    for n in range(orden + 1):
        valor_aproximado += (-x)**n / math.factorial(n)
    return valor_aproximado

x_original = 0.505

x_referencia = 0.5

valor_real = math.exp(-x_original)

for orden in range(16):
    valor_aproximado = calcular_valor_taylor(x_referencia, orden)
    error_relativo_porcentual = abs((valor_real - valor_aproximado) / valor_real) * 100
    print(f"Orden {orden}: Valor Aproximado = {valor_aproximado}, Error Relativo Porcentual = {error_relativo_porcentual}%")
