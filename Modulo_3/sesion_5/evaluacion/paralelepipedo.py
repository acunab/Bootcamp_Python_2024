# Palabra inicial
palabra = "paralelepípedo"

# Vocales
vocales = "aeiouáéíóú"

# Recorremos la palabra y verificamos cada carácter
for posicion, letra in enumerate(palabra):
    if letra not in vocales:
        print(f"Consonante: {letra}, Posición: {posicion}")