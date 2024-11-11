 #             Persona
#            /    |    \
#  Futbolista  Entrenador  Masajista

# Clase base Persona
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def describir(self):
        return f"{self.nombre}, {self.edad} años, Nacionalidad: {self.nacionalidad}"

# Clase Futbolista que hereda de Persona
class Futbolista(Persona):
    def __init__(self, nombre, edad, nacionalidad, posicion, numero, goles):
        super().__init__(nombre, edad, nacionalidad)
        self.posicion = posicion
        self.numero = numero
        self.goles = goles

    def jugar_partido(self):
        return f"{self.nombre} está jugando en la posición de {self.posicion} con el número {self.numero}."

    def entrenar(self):
        return f"{self.nombre} está entrenando para el próximo partido."

# Clase Entrenador que hereda de Persona
class Entrenador(Persona):
    def __init__(self, nombre, edad, nacionalidad, estrategia, experiencia):
        super().__init__(nombre, edad, nacionalidad)
        self.estrategia = estrategia
        self.experiencia = experiencia

    def planificar_entrenamiento(self):
        return f"{self.nombre} está planificando el entrenamiento con la estrategia {self.estrategia}."

    def dirigir_partido(self):
        return f"{self.nombre} está dirigiendo el partido."

# Clase Masajista que hereda de Persona
class Masajista(Persona):
    def __init__(self, nombre, edad, nacionalidad, especialidad, experiencia):
        super().__init__(nombre, edad, nacionalidad)
        self.especialidad = especialidad
        self.experiencia = experiencia

    def dar_masaje(self):
        return f"{self.nombre} está dando un masaje de {self.especialidad}."

    def preparar_partido(self):
        return f"{self.nombre} está preparando a los jugadores para el partido."

# Ejemplos de uso
futbolista = Futbolista("Lionel Messi", 34, "Argentina", "Delantero", 10, 30)
entrenador = Entrenador("Pep Guardiola", 50, "España", "Posesión", 15)
masajista = Masajista("Juan Pérez", 40, "España", "Rehabilitación", 20)

print(futbolista.describir())
print(futbolista.jugar_partido())
print(entrenador.describir())
print(entrenador.planificar_entrenamiento())
print(masajista.describir())
print(masajista.dar_masaje())