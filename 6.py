import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator

# Definición de la función objetivo
def funcion_objetivo(x):
    return 1 / (1 + x**2)

# Generación de puntos de muestra en el intervalo [-5, 5]
puntos_x = np.linspace(-5, 5, 11)
puntos_y = funcion_objetivo(puntos_x)

# Creación del interpolador polinómico
interpolador_polinomico = BarycentricInterpolator(puntos_x, puntos_y)

# Evaluación del polinomio interpolado en x = 2.8
punto_a_evaluar = 2.8
valor_interpolado = interpolador_polinomico(punto_a_evaluar)

# Cálculo del valor real de la función en x = 2.8
valor_real = funcion_objetivo(punto_a_evaluar)

# Impresión de los resultados
print(f"Valor de la interpolacion de f({punto_a_evaluar}): {valor_interpolado}")
print(f"Valor real de f({punto_a_evaluar}): {valor_real}")

# Visualización para comparar el polinomio interpolado con la función real
rango_x = np.linspace(-5, 5, 500)
funcion_real = funcion_objetivo(rango_x)
funcion_interpolada = interpolador_polinomico(rango_x)

plt.plot(rango_x, funcion_real, label="Función Real f(x)")
plt.plot(rango_x, funcion_interpolada, '--', label="Polinomio Interpolado")
plt.scatter(puntos_x, puntos_y, color='red', label="Puntos de Interpolación")
plt.scatter([punto_a_evaluar], [valor_interpolado], color='green', label=f"f({punto_a_evaluar}) Interpolado")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Interpolación Polinómica de Grado 10")
plt.grid(True)
plt.show()
