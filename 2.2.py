import numpy as np
from scipy.interpolate import lagrange

# Datos del primer grupo
horas_grupo1 = np.array([6, 8, 10, 12])
temperaturas_grupo1 = np.array([7, 9, 12, 18])

# Crear el polinomio de Lagrange para el primer grupo
polinomio_grupo1 = lagrange(horas_grupo1, temperaturas_grupo1)

# Evaluar el polinomio en las horas 7:00 y 9:00
evaluacion_7 = polinomio_grupo1(7)
evaluacion_9 = polinomio_grupo1(9)

# Datos del segundo grupo
horas_grupo2 = np.array([14, 16, 18, 20])
temperaturas_grupo2 = np.array([21, 19, 15, 10])

# Crear el polinomio de Lagrange para el segundo grupo
polinomio_grupo2 = lagrange(horas_grupo2, temperaturas_grupo2)

# Evaluar el polinomio en las horas 12:30 y 18:10
evaluacion_12_30 = polinomio_grupo2(12.5)
evaluacion_18_10 = polinomio_grupo2(18.1)

# Imprimir resultados
print(f"Temperatura estimada a las 7:00: {evaluacion_7:.2f} °C")
print(f"Temperatura estimada a las 9:00: {evaluacion_9:.2f} °C")
print(f"Temperatura estimada a las 12:30: {evaluacion_12_30:.2f} °C")
print(f"Temperatura estimada a las 18:10: {evaluacion_18_10:.2f} °C")
