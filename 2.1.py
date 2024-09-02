import numpy as np

# Función para calcular el polinomio de Lagrange
def lagrange_polynomial(x_vals, y_vals):
    def polynomial(x):
        result = 0
        n = len(x_vals)
        for i in range(n):
            term = y_vals[i]
            for j in range(n):
                if i != j:
                    term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
            result += term
        return result
    
    return polynomial

# Datos
horas = np.array([6, 8, 10, 12, 14, 16, 18, 20])
temperaturas = np.array([7, 9, 12, 18, 21, 19, 15, 10])

# Crear el polinomio de Lagrange
P = lagrange_polynomial(horas, temperaturas)

# Estimar las temperaturas para las horas solicitadas
horas_estimadas = [7, 9, 12.5, 18.1667]
temperaturas_estimadas = [P(h) for h in horas_estimadas]

for h, t in zip(horas_estimadas, temperaturas_estimadas):
    print(f"Temperatura estimada a las {h:.2f} horas: {t:.2f} °C")
