import numpy as np
import matplotlib.pyplot as plt

def parabola(a, b, c, x):
    return a * x**2 + b * x + c

a=1
b=2
c=1

x = np.linspace(-10, 10, 50)  

y = parabola(a, b, c, x)


plt.plot(x, y, label=f'Parábola: $y = {a}x^2 + {b}x + {c}$')
plt.title("Gráfico de una parábola")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black',linewidth=0.5) 
plt.axvline(0, color='black',linewidth=0.5)  
plt.grid(True)  
plt.legend() 
plt.show()  
