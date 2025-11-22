# --- 1. Constantes y Configuración ---
USUARIO_CORRECTO = "admin"
CLAVE_CORRECTA = "1234"
MAX_INTENTOS = 3

# Variable que almacena la clave actual (permite que se modifique en el menú)
contrasena_actual = CLAVE_CORRECTA

# --- 2. LOGIN CON LÍMITE DE INTENTOS (BUCLE FOR) ---
print("--- SISTEMA DE CONTROL DE ACCESO ---")
acceso_concedido = False

for intento in range(MAX_INTENTOS):
    print(f"\n--- Intento {intento + 1} de {MAX_INTENTOS} ---")
    usuario = input("Introduce tu usuario: ")
    contrasena = input("Introduce tu contraseña: ")

    if usuario == USUARIO_CORRECTO and contrasena == contrasena_actual:
        print("\nAcceso concedido.")
        acceso_concedido = True
        break  # Rompe el bucle FOR de intentos al tener éxito
    else:
        print("Usuario o contraseña incorrectos.")

# --- 3. MENÚ PRINCIPAL (BUCLE WHILE) ---
if acceso_concedido:
    while True:
        print("\n----- MENÚ PRINCIPAL -----")
        print("1. Ver perfil")
        print("2. Cambiar contraseña")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print(f"\nPerfil: {USUARIO_CORRECTO}")
            print(f"Clave actual (simulada): {contrasena_actual}")

        elif opcion == "2":
            nueva = input("Introduce la nueva contraseña: ")
            contrasena_actual = nueva  # Actualizamos la clave
            print("Contraseña cambiada con éxito.")

        elif opcion == "3":
            print("Cerrando sesión. ¡Hasta pronto!")
            break  # Rompe el bucle WHILE y finaliza el programa

        else:
            print("Opción no válida. Inténtalo de nuevo.")

else:
    # Este bloque se ejecuta si el bucle FOR de arriba termina sin el 'break'
    print("\nSe ha superado el límite de intentos. Acceso bloqueado.")