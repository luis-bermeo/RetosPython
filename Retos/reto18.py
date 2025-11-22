# Pide un importe y muestra cuántos billetes de cada tipo se necesitan.
try:
    importe = int(input("Introduce el importe a retirar: "))
except ValueError:
    print("Error: Ingresa un número entero válido.")
    exit()

billetes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
importe_original = importe

if importe <= 0:
    print("El importe debe ser positivo.")
else:
    print(f"\nDesglose de {importe_original}€:")
    for billete in billetes:
        # División entera para saber cuántos billetes caben
        cantidad = importe // billete

        if cantidad > 0:
            print(f"{cantidad} x {billete}€")

        # Módulo para actualizar el importe restante
        importe %= billete

