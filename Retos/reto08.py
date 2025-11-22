# Crea un menú con opciones que se repita hasta que el usuario elija salir.
while True:
    print("\n--- MENÚ INTERACTIVO ---")
    print("1. Saludar")
    print("2. Sumar")
    print("3. Salir")
    opcion = input("Elige una opción (1-3): ")

    if opcion == '1':
        print("¡Hola! Bienvenido al sistema.")
    elif opcion == '2':
        try:
            a = int(input("Primer número: "))
            b = int(input("Segundo número: "))
            print(f"La suma es: {a + b}")
        except ValueError:
            print("Error: Ingresa números válidos.")
    elif opcion == '3':
        print("Saliendo del programa. ¡Hasta pronto!")
        break
    else:
        print("Opción inválida. Intenta con 1, 2 o 3.")