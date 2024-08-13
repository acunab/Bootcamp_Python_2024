# Número para calcular el factorial
numero = 5

# Inicializar la variable para el factorial
factorial = 1

# Calcular el factorial usando un bucle
for i in range(1, numero + 1):
    factorial *= i

# Imprimir el resultado
print(f"El factorial de {numero} es: {factorial}")