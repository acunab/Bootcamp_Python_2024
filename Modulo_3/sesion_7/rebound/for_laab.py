# Crear una lista con 10 números enteros
numeros = [12, 7, 0, 5, 24, 13, 6, 0, 8, 19]

# Recorrer la lista usando un bucle for
for numero in numeros:
    if numero == 0:
        print(f"El número {numero} es cero.")
    elif numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")