import math
def area_circulo():
    r=int(input("Dime el radio del circulo cuya área quieres calcular:"))
    A= math.pi *r**2
    return A
area = area_circulo()
print(f"El área del círculo es: {area}")
