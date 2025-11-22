# Permite 3 intentos para introducir usuario y contraseña correctos.
usuario_valido = "admin"
clave_valida = "1234"
MAX_INTENTOS = 3

for intento in range(1, MAX_INTENTOS + 1):
    user = input(f"Intento {intento}/{MAX_INTENTOS} - Usuario: ")
    pwd = input(f"Intento {intento}/{MAX_INTENTOS} - Contraseña: ")

    if user == usuario_valido and pwd == clave_valida:
        print("Acceso concedido. ¡Bienvenido!")
        break
    else:
        if intento < MAX_INTENTOS:
            print(f"Credenciales incorrectas. Te quedan {MAX_INTENTOS - intento} intentos.")
        else:
            print("Demasiados intentos fallidos. Cuenta bloqueada.")