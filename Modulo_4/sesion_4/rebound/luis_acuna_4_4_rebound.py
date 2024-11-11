# Definición de la clase Libro (sin atributos iniciales en el constructor)
class Libro:
    pass

# Creación de las instancias de la clase Libro
libro_1 = Libro()
libro_2 = Libro()

# Asignación de atributos a cada instancia
libro_1.autor = 'Dan Brown'
libro_1.titulo = 'Infierno'

libro_2.autor = 'Dan Brown'
libro_2.titulo = 'El Código Da Vinci'
libro_2.ann_de_publicacion = 2003

# Imprimir el diccionario de atributos de cada instancia
print(libro_1.__dict__)
print(libro_2.__dict__)