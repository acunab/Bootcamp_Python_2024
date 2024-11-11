# Clase base Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def movimiento(self):
        return "caminando"

# Subclase Maratonista que hereda de Persona
class Maratonista(Persona):
    def movimiento(self):
        return "trotando"

# Subclase Ciclista que hereda de Persona
class Ciclista(Persona):
    def movimiento(self):
        return "rodando"

# Ejemplo de uso
persona = Persona("Juan")
maratonista = Maratonista("Carlos")
ciclista = Ciclista("Ana")

# Imprimir los estados de movimiento de cada instancia
print(f"{persona.nombre} está {persona.movimiento()}.")
print(f"{maratonista.nombre} está {maratonista.movimiento()}.")
print(f"{ciclista.nombre} está {ciclista.movimiento()}.")