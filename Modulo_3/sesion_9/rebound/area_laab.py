def calcular_area_rectangulo(base, altura):
    # Validar que ambos sean números y positivos
    if isinstance(base, (int, float)) and isinstance(altura, (int, float)):
        if base > 0 and altura > 0:
            # Calcular el área
            area = base * altura
            return area
        else:
            return "Error: La base y la altura deben ser números positivos."
    else:
        return "Error: La base y la altura deben ser números."

# Ejemplo de uso
resultado = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {resultado}")