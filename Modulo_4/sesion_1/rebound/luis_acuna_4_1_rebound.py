class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def comer(self):
        return f"{self.nombre} está comiendo."

    def caminar(self):
        return f"{self.nombre} está caminando."

    def dormir(self):
        return f"{self.nombre} está durmiendo."
    
# Crear el objeto perro
perro = Animal(nombre="Brando", raza="San Bernardo", edad=3, peso=30)

# Crear el objeto gato
gato = Animal(nombre="Roll", raza="Persa", edad=4, peso=3)

# Perro
print(perro.comer())  # Brando está comiendo.
print(perro.caminar())  # Brando está caminando.
print(perro.dormir())  # Brando está durmiendo.

# Gato
print(gato.comer())  # Roll está comiendo.
print(gato.caminar())  # Roll está caminando.
print(gato.dormir())  # Roll está durmiendo.