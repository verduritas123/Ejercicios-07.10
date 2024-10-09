import numpy as np
import matplotlib.pyplot as plt

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return None
    raiz1 = (-b + np.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - np.sqrt(discriminante)) / (2*a)
    return raiz1, raiz2

def graficar_funcion_cuadratica(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    raices = resolver_ecuacion_cuadratica(a, b, c)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=f'$y = {a}x^2 + {b}x + {c}$', color='blue')
    
    if raices:
        for raiz in raices:
            plt.plot(raiz, 0, 'ro')
            plt.annotate(f'Raíz: {raiz:.2f}', xy=(raiz, 0), xytext=(raiz, 10), 
                         arrowprops=dict(facecolor='black', shrink=0.05))

    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.title('Gráfica de la Función Cuadrática')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.ylim(-10, 10)
    plt.show()

a = 1
b = -3
c = 2

graficar_funcion_cuadratica(a, b, c)
