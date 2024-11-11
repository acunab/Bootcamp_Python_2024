# Clase Persona
class Persona:
    def __init__(self, nombre, apellido, anno):
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno

# Clase Departamento
class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto):
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto

# Clase Trabajador, que hereda de Persona y Departamento
class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, anno, nombre_dpto, nombre_corto_dpto, salario):
        # Inicialización de los atributos de Persona y Departamento
        Persona.__init__(self, nombre, apellido, anno)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        self.salario = salario

# Creación del objeto trabajador con los datos especificados
trabajador = Trabajador("Juan", "Pérez", 2005, "Ingeniería de software", "IS", 20000)

# Imprimir los atributos del objeto trabajador usando __dict__
print(trabajador.__dict__)

# Verificar la instancia de trabajador
print(isinstance(trabajador, Persona))       # Debería imprimir True
print(isinstance(trabajador, Departamento))  # Debería imprimir True
print(isinstance(trabajador, Trabajador))    # Debería imprimir True