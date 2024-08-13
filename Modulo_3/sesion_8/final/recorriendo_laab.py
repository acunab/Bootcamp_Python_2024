# Lista de listas
lista_de_listas = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

# Diccionario que almacenará las sublistas
diccionario = {}

# Claves para el diccionario
claves = ['A', 'B', 'C', 'D']

# Recorrer la lista de listas
for i, sublista in enumerate(lista_de_listas):
    # Si el primer elemento es 0, omitimos la sublista completa
    if sublista[0] == 0:
        continue
    
    # Filtramos la sublista para eliminar cualquier cero que no sea el primero
    sublista_filtrada = [x for x in sublista if x != 0]
    
    # Asignamos la sublista filtrada al diccionario
    diccionario[claves[i]] = sublista_filtrada
    
    # Imprimimos la sublista filtrada
    print(f"{claves[i]}:{sublista_filtrada}")

# Finalmente, imprimimos el diccionario completo
print("Diccionario resultante:", diccionario)