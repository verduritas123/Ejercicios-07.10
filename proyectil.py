import numpy as np
import matplotlib.pyplot as plt

def simular_proyectil(velocidad_inicial, angulo, tiempo_max):
    g = 9.81
    angulo_rad = np.radians(angulo)
    t = np.linspace(0, tiempo_max, num=100)
    x = velocidad_inicial * np.cos(angulo_rad) * t
    y = velocidad_inicial * np.sin(angulo_rad) * t - (0.5 * g * t**2)
    return x, y

velocidad_inicial = 50
tiempo_max = 10
angulos = [30, 45, 60]

plt.figure(figsize=(10, 5))
for angulo in angulos:
    x, y = simular_proyectil(velocidad_inicial, angulo, tiempo_max)
    plt.plot(x, y, label=f'Ángulo: {angulo}°')

plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.title('Trayectorias de Proyectiles')
plt.xlabel('Distancia (m)')
plt.ylabel('Altura (m)')
plt.grid()
plt.legend()
plt.ylim(0, 30)
plt.show()

