import os

# Nombre del archivo
archivo = "informacion.dat"

# Verificar si el archivo ya existe
if os.path.exists(archivo):
    print("El archivo ya se encuentra previamente creado.")
else:
    # Crear el archivo y escribir las líneas de información
    with open(archivo, "w") as file:
        file.write("Datos de información en la línea 1\n")
        file.write("Datos de información en la línea 2\n")
        file.write("Datos de información en la línea 3\n")
        file.write("Datos de información en la línea 4\n")
        file.write("Datos de información en la línea 5\n")
    print("Archivo creado exitosamente con la información.")