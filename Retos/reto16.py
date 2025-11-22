# Juego donde el usuario tiene que adivinar un número secreto entre 1 y 100.
import random
secreto = random.randint(1, 100)
intentos = 0
print("--- Adivina el Número (1-100) ---")

while True:
    try:
        intento = int(input("Tu intento: "))
        intentos += 1

        if intento == secreto:
            print(f"¡Felicidades! Adivinaste el número {secreto} en {intentos} intentos.")
            break
        elif intento < secreto:
            print("El número secreto es MÁS ALTO.")
        else:
            print("El número secreto es MÁS BAJO.")
    except ValueError:
        print("Por favor, introduce un número válido.")