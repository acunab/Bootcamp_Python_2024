import os

# Nombre del archivo
archivo = "informacion.dat"

def crear_archivo():
    """Crea el archivo informacion.dat con líneas de datos si no existe."""
    if os.path.exists(archivo):
        print("El archivo informacion.dat ya existe, ha sido creado previamente")
    else:
        # Crear el archivo y escribir las líneas de información
        with open(archivo, "w") as file:
            file.write("Datos de información en la línea 1\n")
            file.write("Datos de información en la línea 2\n")
            file.write("Datos de información en la línea 3\n")
            file.write("Datos de información en la línea 4\n")
            file.write("Datos de información en la línea 5\n")
        print("Archivo creado exitosamente con la información.")

def leer_archivo():
    """Lee y muestra el contenido del archivo informacion.dat si existe."""
    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            contenido = file.read()
            print(contenido)
    else:
        print("El archivo no existe.")

# Ejecución del programa
crear_archivo()
leer_archivo()