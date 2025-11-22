# Pide un número y determina si es primo usando un bucle.
num = int(input("Introduce un número entero: "))

if num <= 1:
    print(f"{num} no es un número primo.")
else:
    es_primo = True
    # Solo necesitamos verificar divisores hasta la raíz cuadrada del número
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")