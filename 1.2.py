import numpy as np
import sympy as sp

# Datos
years = np.array([1964, 1973, 1981, 2002])
population = np.array([4.28, 5.16, 6.05, 11.24])

# Definimos la variable simbólica
x = sp.symbols('x')

# Inicializamos el polinomio de Lagrange
lagrange_polynomial = 0

# Calculamos el polinomio de Lagrange
for i in range(len(years)):
    term = population[i]
    for j in range(len(years)):
        if i != j:
            term *= (x - years[j]) / (years[i] - years[j])
    lagrange_polynomial += term

# Simplificamos el polinomio
lagrange_polynomial = sp.simplify(lagrange_polynomial)

# Mostramos el polinomio resultante
print("Polinomio de Lagrange:")
print(lagrange_polynomial)

# Convertimos el polinomio a una función utilizable
polynomial_func = sp.lambdify(x, lagrange_polynomial, 'numpy')

# Años a estimar
years_to_estimate = [1976, 2000]

# Estimaciones de la población
estimated_populations = [polynomial_func(year) for year in years_to_estimate]

# Mostramos las estimaciones
print(f"\nEstimación de la población en 1976: {estimated_populations[0]:.2f} millones de personas")
print(f"Estimación de la población en 2000: {estimated_populations[1]:.2f} millones de personas")
