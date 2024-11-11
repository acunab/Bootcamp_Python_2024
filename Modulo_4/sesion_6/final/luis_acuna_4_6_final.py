usuarios = {'001': 'Marca', '002': 'Mónica', '003': 'Jacob'}
id_usuario = '004'

try:
    # Intentar acceder a la clave '004'
    print(usuarios[id_usuario])
except KeyError:
    # Mensaje y adición de la clave si ocurre KeyError
    print(f"La clave {id_usuario} no está en el diccionario. Añadiendo clave...")
    usuarios[id_usuario] = 'Ninguno'

# Imprimir el diccionario actualizado
print(usuarios)