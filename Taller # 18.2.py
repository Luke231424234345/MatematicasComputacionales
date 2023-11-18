import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos proporcionados
x = np.array([1, 3, 5, 7, 9, 11, 13, 15])
y = np.array([8.5, 13, 15, 16, 17, 17.5, 18, 19])

# Definir la función de razón de crecimiento
def growth_ratio(x, a, b):
    return a + b * x

# Aplicar regresión de razón de crecimiento por mínimos cuadrados
params_growth, covariance_growth = curve_fit(growth_ratio, x, y)

# Obtener los parámetros ajustados
a_growth, b_growth = params_growth

# Graficar los puntos y la curva ajustada
plt.scatter(x, y, label='Datos')
plt.plot(x, growth_ratio(x, a_growth, b_growth), 'g', label='Modelo de Razón de Crecimiento Ajustado')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Regresión de Razón de Crecimiento')
plt.show()
