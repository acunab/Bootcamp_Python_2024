#Requerimos crear un registro de datos personales de tres personas. Los datos que se necesitan
#son: su nombre, apellido y teléfono. Para ello, generaremos un diccionario para cada una de las 
#personas con los datos mencionados, y luego los almacenaremos dentro de una lista. Finalmente, 
#imprimiremos en pantalla la lista

# Crear diccionarios para cada persona con sus datos
persona1 = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "telefono": "123456789"
}

persona2 = {
    "nombre": "María",
    "apellido": "García",
    "telefono": "987654321"
}

persona3 = {
    "nombre": "Carlos",
    "apellido": "Rodríguez",
    "telefono": "555555555"
}

# Crear una lista que contenga los diccionarios de las tres personas
lista_personas = [persona1, persona2, persona3]

# Imprimir la lista completa
print(lista_personas)