import matplotlib.pyplot as plt

# Datos
presion = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
volumen = [1.62, 1.0, 0.75, 0.62, 0.52, 0.46]

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(presion, volumen, 'bo-', label="Datos")
plt.xlabel("Presión (x)")
plt.ylabel("Volumen (y)")
plt.title("Relación entre Volumen y Presión")
plt.grid(True)
plt.legend()
plt.show()
