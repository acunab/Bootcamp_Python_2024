while True:
    try:
        edad = int(input("Por favor, ingrese su edad: "))
        break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

# Verificar si es adulto o no
if edad >= 18:
    print("Es adulto.")
else:
    print("No es adulto.")