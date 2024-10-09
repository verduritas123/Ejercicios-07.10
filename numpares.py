n= int(input("Dime hasta cuántos primeros números pares quiere sumar:"))
def numpares():
    num=2
    while num < 2*n:
        num+=2+num
    return num
suma= numpares()
print(f"La suma de los {n} primeros números pares es: {suma}")