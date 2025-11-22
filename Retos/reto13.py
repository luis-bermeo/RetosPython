# Dada una lista de nombres de archivo, muestra solo los .pdf.
archivos = ["documento.docx", "informe_final.pdf", "imagen.jpg", "datos.pdf"]
print("Archivos PDF encontrados:")
for archivo in archivos:
    if archivo.endswith(".pdf"):
        print(archivo)