import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
X = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([7, 5, 6, 3, 4, 2.5, 2])

# Aplicar regresión lineal por mínimos cuadrados
A = np.vstack([X, np.ones(len(X))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

# Imprimir los coeficientes de la línea ajustada
print(f"La línea ajustada es: y = {m:.2f}x + {c:.2f}")

# Graficar los puntos y la línea ajustada
plt.scatter(X, y, label='Datos')
plt.plot(X, m*X + c, 'r', label='Línea ajustada')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
