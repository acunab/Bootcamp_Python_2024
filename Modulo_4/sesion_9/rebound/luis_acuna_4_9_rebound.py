import os

# Nombre del archivo
archivo = "informacion.dat"

def crear_o_verificar_archivo():
    """Crea el archivo con contenido inicial si no existe, y si ya existe muestra un mensaje."""
    if os.path.exists(archivo):
        print("El archivo informacion.dat ya existe, ha sido creado previamente")
    else:
        with open(archivo, "w") as file:
            # Contenido inicial
            file.write("Datos de información en la línea 1\n")
            file.write("Datos de información en la línea 2\n")
            file.write("Datos de información en la línea 3\n")
            file.write("Datos de información en la línea 4\n")
            file.write("Datos de información en la línea 5\n")
        print("Archivo creado exitosamente con la información inicial.")

def agregar_contenido():
    """Agrega el nuevo contenido al archivo informacion.dat."""
    with open(archivo, "a") as file:
        # Contenido adicional a agregar
        file.write("Hola Mundo\n")
        file.write("Este en una nueva línea en el archivo\n")
        file.write("agregando la segunda línea del archivo\n")
        file.write("finalizando la línea agregada\n")

def leer_archivo():
    """Lee y muestra el contenido del archivo informacion.dat."""
    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            contenido = file.read()
            print("El nuevo archivo contiene la siguiente información:")
            print(contenido)
    else:
        print("El archivo no existe.")

# Ejecución del programa
crear_o_verificar_archivo()
agregar_contenido()
leer_archivo()