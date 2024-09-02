import numpy as np

# Últimos cuatro valores de la tabla
x = np.array([1981, 1994, 2002, 2018])
y = np.array([6.05, 8.33, 11.24, 14.90])

def lagrange_polynomial(x, y, xp):
    yp = 0
    n = len(x)
    for i in range(n):
        li = 1
        for j in range(n):
            if i != j:
                li *= (xp - x[j]) / (x[i] - x[j])
        yp += y[i] * li
    return yp

# Predicción para 2024 usando el polinomio de Lagrange
poblacion_2024 = lagrange_polynomial(x, y, 2024)
print(f"Población estimada para 2024: {poblacion_2024:.2f} millones de personas")
