# Definir la función f(x)
def f(x):
    return 0.15 * x**4 - 0.25 * x**2 + 3.5

# Valor verdadero de la primera y segunda derivada en x = 0.6
x_true = 0.6
f_prime_true = 0.6**3 - 0.25 * 0.6
f_double_prime_true = 3 * 0.6**2 - 0.25

# Aproximación de la primera derivada hacia adelante con h = 0.1
h = 0.1
f_prime_forward = (f(x_true + h) - f(x_true)) / h

# Aproximación de la primera derivada hacia atrás con h = 0.1
f_prime_backward = (f(x_true) - f(x_true - h)) / h

# Aproximación de la primera derivada centrada con h = 0.1
f_prime_centered = (f(x_true + h) - f(x_true - h)) / (2 * h)

# Aproximación de la segunda derivada centrada con h = 0.1
f_double_prime_centered = (f(x_true + h) - 2 * f(x_true) + f(x_true - h)) / h**2

# Imprimir resultados para h = 0.1
print("Resultados con h = 0.1:")
print(f"Valor verdadero de la primera derivada: {f_prime_true}")
print(f"Aproximación hacia adelante de la primera derivada: {f_prime_forward}")
print(f"Aproximación hacia atrás de la primera derivada: {f_prime_backward}")
print(f"Aproximación centrada de la primera derivada: {f_prime_centered}")
print(f"Valor verdadero de la segunda derivada: {f_double_prime_true}")
print(f"Aproximación centrada de la segunda derivada: {f_double_prime_centered}")

# Aproximaciones para h = 0.05
h = 0.05
f_prime_centered_h05 = (f(x_true + h) - f(x_true - h)) / (2 * h)
f_double_prime_centered_h05 = (f(x_true + h) - 2 * f(x_true) + f(x_true - h)) / h**2

# Imprimir resultados para h = 0.05
print("\nResultados con h = 0.05:")
print(f"Aproximación centrada de la primera derivada con h = 0.05: {f_prime_centered_h05}")
print(f"Aproximación centrada de la segunda derivada con h = 0.05: {f_double_prime_centered_h05}")
