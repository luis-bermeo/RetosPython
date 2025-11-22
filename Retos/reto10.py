# Muestra solo los que empiezan por vocal.
alumnos = ["Ana", "Pedro", "Elena", "Omar", "Luis", "Iván"]
vocales = ('a', 'e', 'i', 'o', 'u')
print("Alumnos que empiezan por vocal:")
for nombre in alumnos:
    # Usamos .lower() y .startswith() para la comprobación
    if nombre.lower().startswith(vocales):
        print(nombre)