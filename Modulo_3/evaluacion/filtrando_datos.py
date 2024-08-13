# Lista de nombres
nombres = [
    "Harry Houdini", 
    "Newton", 
    "David Blaine", 
    "Hawking", 
    "Messi", 
    "Teller", 
    "Einstein", 
    "Pele", 
    "Juanes"
]

# Función para separar los nombres en grupos
def separar_nombres(nombres):
    magos = []
    cientificos = []
    otros = []
    
    for nombre in nombres:
        if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
            magos.append(nombre)
        elif nombre in ["Newton", "Hawking", "Einstein"]:
            cientificos.append(nombre)
        else:
            otros.append(nombre)
    
    return magos, cientificos, otros

# Función para hacer grandiosos a los magos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

# Función para imprimir los nombres
def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

# Separar los nombres en magos, científicos y otros
magos, cientificos, otros = separar_nombres(nombres)

# Imprimir la lista completa de nombres antes de ser modificada
print("Lista completa de nombres:")
imprimir_nombres(nombres)
print("\n")

# Hacer grandiosos a los magos
hacer_grandioso(magos)

# Imprimir los nombres de los magos grandiosos
print("Magos grandiosos:")
imprimir_nombres(magos)
print("\n")

# Imprimir los nombres de los científicos
print("Científicos:")
imprimir_nombres(cientificos)
print("\n")

# Imprimir los nombres restantes
print("Otros:")
imprimir_nombres(otros)