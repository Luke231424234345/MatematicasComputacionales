import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([0.2, 0.5, 1.8, 3.4, 5.7, 9.0, 13.8])

# Calcular la regresión lineal
slope, intercept = np.polyfit(x, y, 1)

# Calcular los valores ajustados (y_pred)
y_pred = slope * x + intercept

# Calcular la desviación estándar (sy)
sy = np.std(y, ddof=1)

# Calcular el error estándar de la estimación (s Τ y x )
s_te = np.sqrt(np.sum((y - y_pred) ** 2) / (len(x) - 2))

# Calcular el coeficiente de correlación (r)
r = np.corrcoef(x, y)[0, 1]

# Imprimir los resultados
print(f"Desviación estándar (sy): {sy:.4f}")
print(f"Error estándar de la estimación (s Τ y x ): {s_te:.4f}")
print(f"Coeficiente de correlación (r): {r:.4f}")

# Graficar los puntos y la regresión lineal
plt.scatter(x, y, label='Datos')
plt.plot(x, y_pred, 'r', label=f'Regresión Lineal: y = {slope:.4f}x + {intercept:.4f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Regresión Lineal y Estadísticas')
plt.show()
