import numpy as np

# Datos de entrada
x = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
y = np.array([1.62, 1.0, 0.75, 0.62, 0.52, 0.46])

# Número de puntos
n = len(x)

# Inicialización de la tabla de diferencias divididas
div_diff = np.zeros((n, n))
div_diff[:, 0] = y

# Cálculo de las diferencias divididas
for j in range(1, n):
    for i in range(n - j):
        div_diff[i][j] = (div_diff[i+1][j-1] - div_diff[i][j-1]) / (x[i+j] - x[i])

# Imprimir los coeficientes de las diferencias divididas
print("Coeficientes de las diferencias divididas:")
for i in range(n):
    print(f"b[{i}] = {div_diff[0][i]}")

# Función para evaluar el polinomio de Newton en x_val
def newton_polynomial(x, x_data, div_diff):
    n = len(x_data)
    result = div_diff[0, 0]
    term = 1.0
    for i in range(1, n):
        term *= (x - x_data[i-1])
        result += div_diff[0, i] * term
    return result

# Valor de x donde se quiere evaluar el polinomio
x_val = 1.75

# Evaluación del polinomio
y_val = newton_polynomial(x_val, x, div_diff)
print(f"\nEl valor del polinomio en x = {x_val} es y = {y_val}")
