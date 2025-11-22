# Recorre una lista de números y busca el 0. Si no lo encuentra, muestra un mensaje con else.
lista_numeros = [1, 5, 8, 12, 44, 9]
print(f"Buscando el 0 en la lista: {lista_numeros}")
for num in lista_numeros:
    if num == 0:
        print("¡Cero encontrado!")
        break
else:
    # Este bloque solo se ejecuta si el bucle termina SIN el 'break'.
    print("El número 0 no está en la lista.")