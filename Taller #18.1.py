import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos proporcionados
x = np.array([1, 3, 5, 7, 9, 11, 13, 15])
y = np.array([8.5, 13, 15, 16, 17, 17.5, 18, 19])

# Definir la función de ecuación de potencias
def power_equation(x, a, b):
    return a * (x ** b)

# Aplicar regresión de ecuación de potencias por mínimos cuadrados
params_power, covariance_power = curve_fit(power_equation, x, y)

# Obtener los parámetros ajustados
a_power, b_power = params_power

# Graficar los puntos y la curva ajustada
plt.scatter(x, y, label='Datos')
plt.plot(x, power_equation(x, a_power, b_power), 'r', label='Modelo de Ecuación de Potencias Ajustado')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Regresión de Ecuación de Potencias')
plt.show()
