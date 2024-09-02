import numpy as np
import matplotlib.pyplot as plt

# Definir el polinomio de Lagrange
def P(x):
    return (23/6)*x**4 - 138*x**3 + (5474/3)*x**2 - 10488*x + 22080

# Valores de x (horas)
x_vals = np.linspace(5, 13, 400)  # Valores de x desde 5 hasta 13 (para una gráfica más completa)

# Valores de y (temperaturas) calculados usando el polinomio de Lagrange
y_vals = P(x_vals)

# Puntos originales de la tabla
x_points = np.array([6, 8, 10, 12])
y_points = np.array([7, 9, 12, 18])

# Graficar
plt.plot(x_vals, y_vals, label='Polinomio de Lagrange', color='blue')
plt.scatter(x_points, y_points, color='red', label='Puntos originales')
plt.xlabel('Hora')
plt.ylabel('Temperatura (°C)')
plt.title('Polinomio de Lagrange y Puntos Originales')
plt.legend()
plt.grid(True)
plt.show()
