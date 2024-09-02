import numpy as np

puntos_x = np.array([-2, -1, 0, 1, 2, 3])
valores_fx = np.array([1, 4, 11, 16, 13, -4])

def calcular_diferencias_divididas(puntos_x, valores_fx):
    num_puntos = len(valores_fx)
    tabla_coef = np.zeros((num_puntos, num_puntos))
    tabla_coef[:, 0] = valores_fx

    for col in range(1, num_puntos):
        for fila in range(num_puntos - col):
            numerador = tabla_coef[fila + 1, col - 1] - tabla_coef[fila, col - 1]
            denominador = puntos_x[fila + col] - puntos_x[fila]
            tabla_coef[fila, col] = numerador / denominador
    return tabla_coef

tabla_coef = calcular_diferencias_divididas(puntos_x, valores_fx)

print("Tabla de diferencias divididas:")
for i, col in enumerate(tabla_coef.T):
    print(f"Columna {i + 1}: {col}")

def interpolar_newton(tabla_coef, puntos_x, valor):
    resultado = tabla_coef[0, 0]
    producto = 1.0
    for i in range(1, len(puntos_x)):
        producto *= (valor - puntos_x[i - 1])
        resultado += tabla_coef[0, i] * producto
    return resultado

def evaluar_polinomio(valor):
    return interpolar_newton(tabla_coef, puntos_x, valor)

print("\nEvaluación del polinomio en los puntos dados:")
for punto in puntos_x:
    print(f"P({punto}) = {evaluar_polinomio(punto)}")

coincide_con_valores_fx = np.allclose([evaluar_polinomio(punto) for punto in puntos_x], valores_fx)
mensaje_grado = "El polinomio que interpola los datos es de grado 3." if coincide_con_valores_fx else "El polinomio no es de grado 3."
print(f"\n{mensaje_grado}")
