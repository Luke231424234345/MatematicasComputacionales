import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([3.2, 0.4, -1, -1.4, -1.1, 0.6, 3.1])

# Ajustar un polinomio de segundo grado
coefficients = np.polyfit(x, y, 2)

# Crear una función polinómica con los coeficientes encontrados
poly_func = np.poly1d(coefficients)

# Calcular el coeficiente de correlación (r)
r = np.corrcoef(x, y)[0, 1]

# Imprimir los coeficientes y el coeficiente de correlación
print(f"Coeficientes del polinomio: {coefficients}")
print(f"Coeficiente de correlación (r): {r:.4f}")

# Graficar los puntos y el polinomio ajustado
x_values = np.linspace(min(x), max(x), 100)
y_pred = poly_func(x_values)

plt.scatter(x, y, label='Datos')
plt.plot(x_values, y_pred, 'r', label=f'Polinomio de 2º grado ajustado')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Ajuste de Polinomio y Coeficiente de Correlación')
plt.show()
