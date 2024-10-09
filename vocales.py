palabra= input("Dime una palabra para contar el número de vocales:")
vocales= "aeiouAEIOU"
contador=0
for letra in palabra:
    if letra in vocales:
        contador += 1
print(f"Hay {contador} vocales en tu palabra")