import numpy as np

# Valores dados de presión y volumen
x_vals = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
y_vals = np.array([1.62, 1.0, 0.75, 0.62, 0.52, 0.46])

# Valor de presión para extrapolar
x_extrapolate = 3.5

# Extrapolación lineal
y_extrapolate = y_vals[-1] + (x_extrapolate - x_vals[-1]) / (x_vals[-1] - x_vals[-2]) * (y_vals[-1] - y_vals[-2])

print(f"El volumen estimado para una presión de {x_extrapolate} es {y_extrapolate:.2f} unidades de volumen.")
