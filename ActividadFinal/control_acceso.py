# Constantes
USUARIO_CORRECTO = "admin"
CLAVE_CORRECTA = "1234"
MAX_INTENTOS = 3

# Variable para almacenar la contraseña actual
contrasena_actual = CLAVE_CORRECTA

# --- 1. LOGIN CON LÍMITE DE INTENTOS (BUCLE FOR) ---
acceso_concedido = False

for intento in range(MAX_INTENTOS):
    print(f"\n--- Intento {intento + 1} de {MAX_INTENTOS} ---")
    usuario = input("Introduce tu usuario: ")
    contrasena = input("Introduce tu contraseña: ")

    # Comprobación de credenciales
    if usuario == USUARIO_CORRECTO and contrasena == contrasena_actual:
        print("\nAcceso concedido.")
        acceso_concedido = True
        break  # Rompe el bucle FOR de intentos
    else:
        print("Usuario o contraseña incorrectos.")

# --- 2. MENÚ PRINCIPAL (BUCLE WHILE) ---
if acceso_concedido:
    # Este es el bloque donde pegaremos el menú en el Commit 3
    pass
else:
    # Este bloque se ejecuta si el bucle FOR de arriba termina sin un 'break'
    print("\nSe ha superado el límite de intentos. Acceso bloqueado.")