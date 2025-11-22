# Pide una frase y cuenta cuántas palabras contiene.
frase = input("Introduce una frase: ").strip() # .strip() quita espacios al inicio/final

if frase:
    # split() divide la frase por espacios en una lista de palabras
    palabras = frase.split()
    num_palabras = len(palabras)
    print(f"La frase tiene {num_palabras} palabras.")
else:
    print("No se introdujo ninguna palabra.")