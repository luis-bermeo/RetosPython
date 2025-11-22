# Pide una palabra y cuenta cuántas vocales tiene.
palabra = input("Introduce una palabra: ").lower()
contador = 0
for letra in palabra:
    if letra in "aeiou":
        contador += 1
print(f"La palabra '{palabra}' tiene {contador} vocales.")