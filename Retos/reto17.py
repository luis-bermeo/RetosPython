# Muestra una tabla de conversión de °C a °F del 0 al 100 en pasos de 10.
print("--- Tabla de Conversión °C a °F (0° a 100° en pasos de 10) ---")
print("Celsius (°C) \t Fahrenheit (°F)")
print("-" * 35)

for C in range(0, 101, 10):
    # Fórmula de conversión: F = (C * 9/5) + 32
    F = (C * 9/5) + 32
    print(f"{C}\t\t {F}")