contraseña_correcta = "secreto"

while True:

    clave = input("Introduce la contraseña: ")

    if clave == contraseña_correcta:

        print("¡Acceso concedido!")
        break

    else:
        print("Contraseña incorrecta. Intenta de nuevo.")