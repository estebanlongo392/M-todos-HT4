import numpy as np

def newton_interpolation(x_values, y_values, x):
    """Interpolación de Newton para encontrar el valor f(x)"""
    n = len(x_values)
    # Crear tabla de diferencias divididas
    divided_diff = np.zeros((n, n))
    divided_diff[:,0] = y_values
    
    # Llenar la tabla de diferencias divididas
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i+1][j-1] - divided_diff[i][j-1]) / (x_values[i+j] - x_values[i])
    
    # Construir el polinomio de Newton
    result = divided_diff[0, 0]
    product = 1.0
    for i in range(1, n):
        product *= (x - x_values[i-1])
        result += divided_diff[0, i] * product
    
    return result

# Datos del inciso 4
x_values_4 = [1.6, 2.0, 2.5, 3.2, 4.0, 4.5]
y_values_4 = [2, 8, 14, 15, 8, 2]

# Calculando f(2.8) para cada grado
f_2_8_grade_1 = newton_interpolation(x_values_4[:2], y_values_4[:2], 2.8)
f_2_8_grade_2 = newton_interpolation(x_values_4[:3], y_values_4[:3], 2.8)
f_2_8_grade_3 = newton_interpolation(x_values_4[:4], y_values_4[:4], 2.8)

print(f"Inciso 4.1 (Grado 1): f(2.8) = {f_2_8_grade_1}")
print(f"Inciso 4.2 (Grado 2): f(2.8) = {f_2_8_grade_2}")
print(f"Inciso 4.3 (Grado 3): f(2.8) = {f_2_8_grade_3}")
