class SalarioFueraDeRangoError(Exception):
    """Excepción lanzada cuando el salario no está en el rango de 1000 a 2000."""
    def __init__(self, salario, mensaje="El salario no se encuentra en el rango de 1000 a 2000"):
        self.salario = salario
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def validar_salario(salario):
    """Función que valida si el salario está en el rango de 1000 a 2000."""
    if salario < 1000 or salario > 2000:
        raise SalarioFueraDeRangoError(salario)
    else:
        print("El salario está dentro del rango permitido.")

# Ejemplo de uso:
try:
    salario = int(input("Ingrese el salario: "))
    validar_salario(salario)
except SalarioFueraDeRangoError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Ingrese un valor numérico válido.")