# Genera 5 contraseñas aleatorias de 8 caracteres usando un bucle.
import random
import string

print("Generando 5 contraseñas de 8 caracteres:")
for i in range(5):
    # Definimos los posibles caracteres
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Genera 8 caracteres aleatorios y los une
    contraseña = "".join(random.choice(caracteres) for _ in range(8))
    print(f"Contraseña {i+1}: {contraseña}")