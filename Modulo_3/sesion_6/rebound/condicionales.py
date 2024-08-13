# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Verificar si el número es cero
if numero == 0:
    print("El número es cero.")
else:
    # Verificar si el número es positivo o negativo
    if numero > 0:
        print("El número es positivo.")
    else:
        print("El número es negativo.")
    
    # Verificar si el número es par o impar
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")