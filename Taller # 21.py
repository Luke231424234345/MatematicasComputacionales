import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
x1 = np.array([1, 1, 2, 3, 1, 2, 3, 3])
x2 = np.array([0, 1, 1, 2, 2, 3, 3, 1])
y = np.array([1.6, 3, 1.1, 1.3, 3.2, 3.3, 1.8, 0])

# Ajustar una función lineal en dos dimensiones
X = np.vstack((np.ones(len(x1)), x1, x2)).T
coefficients, _, _, _ = np.linalg.lstsq(X, y, rcond=None)

# Calcular el coeficiente de correlación (r)
r = np.corrcoef(np.vstack((x1, x2, y)))[2, 0]

# Imprimir los coeficientes y el coeficiente de correlación
print(f"Coeficientes de la función lineal: {coefficients}")
print(f"Coeficiente de correlación (r): {r:.4f}")

# Graficar los puntos y la función lineal ajustada
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x1, x2, y, label='Datos')
x1_range = np.linspace(min(x1), max(x1), 10)
x2_range = np.linspace(min(x2), max(x2), 10)
x1_range, x2_range = np.meshgrid(x1_range, x2_range)
y_pred = coefficients[0] + coefficients[1] * x1_range + coefficients[2] * x2_range
ax.plot_surface(x1_range, x2_range, y_pred, alpha=0.5, color='r', label='Función Lineal Ajustada')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
plt.legend()
plt.title('Ajuste de Función Lineal y Coeficiente de Correlación')
plt.show()
