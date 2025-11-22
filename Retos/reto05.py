print("Números pares del 1 al 20:")
for i in range(1, 21):
    if i % 2 != 0:
        continue # Salta si el número es impar
    print(i, end=' ')