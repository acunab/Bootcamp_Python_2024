class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    
    def metodo_a(self):
        print("Método heredado de A")

class B:
    def __init__(self):
        print("Clase B")
    
    def metodo_b(self):
        print("Método heredado de B")

# Clase C con herencia múltiple de B y A
class C(B, A):
    def __init__(self):
        super().__init__()  # Llama al constructor de la primera clase en el orden de herencia (B)
        print("Clase C")
    
    def metodo_c(self):
        print("Método de clase C")

# Crear una instancia de C y acceder a los métodos
objeto_c = C()
objeto_c.metodo_a()
objeto_c.metodo_b()
objeto_c.metodo_c()