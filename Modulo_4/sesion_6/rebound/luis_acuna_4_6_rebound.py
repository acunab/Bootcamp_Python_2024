suma = 3000
contador = 0

try:
    resultado = suma / contador
    print(f"El resultado de la división es: {resultado}")
except ZeroDivisionError:
    print("División por cero.")