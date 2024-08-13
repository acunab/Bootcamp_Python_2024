# Solicitar al usuario que ingrese tres números diferentes
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Verificar y ordenar los números de mayor a menor
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"El orden es: {num1}, {num2}, {num3}")
    else:
        print(f"El orden es: {num1}, {num3}, {num2}")
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f"El orden es: {num2}, {num1}, {num3}")
    else:
        print(f"El orden es: {num2}, {num3}, {num1}")
else:
    if num1 > num2:
        print(f"El orden es: {num3}, {num1}, {num2}")
    else:
        print(f"El orden es: {num3}, {num2}, {num1}")