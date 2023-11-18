import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Datos proporcionados
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2.2, 3, 4.5, 6, 8.5, 12])

# Definir la función exponencial
def exponential_model(x, a, b):
    return a * np.exp(b * x)

# Aplicar regresión exponencial por mínimos cuadrados
params, covariance = curve_fit(exponential_model, x, y)

# Obtener los parámetros ajustados
a, b = params

# Imprimir los parámetros de la función exponencial
print(f"La función exponencial ajustada es: y = {a:.2f} * e^({b:.2f} * x)")

# Graficar los puntos y la curva ajustada
plt.scatter(x, y, label='Datos')
plt.plot(x, exponential_model(x, a, b), 'r', label='Modelo Exponencial Ajustado')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
