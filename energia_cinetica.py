def energia_cin():
    m=int(input("Dime la masa de tu particula en kg:"))
    v=int(input("Dime la velocidad de tu particula en m/s:"))
    e_cin= (1/2)*m*v**2
    return e_cin
result = energia_cin()
print(f"La energía cinética de tu partícula es {result} J")