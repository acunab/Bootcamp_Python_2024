import statistics

# Lista de diccionarios que representan información de estudiantes
estudiantes = [
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

# Función para verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Filtrar y mostrar estudiantes con más de 18 años y promedio de calificaciones > 85
print("Estudiantes con más de 18 años y promedio de calificaciones superior a 85:")
for estudiante in estudiantes:
    promedio_calificaciones = statistics.mean(estudiante['calificaciones'])
    if estudiante['edad'] > 18 and promedio_calificaciones > 85:
        print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Promedio de calificaciones: {promedio_calificaciones:.2f}")

# Calcular el promedio de calificaciones de los estudiantes con más de 18 años y edad primo
suma_promedios = 0
contador = 0
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and es_primo(estudiante['edad']):
        promedio_calificaciones = statistics.mean(estudiante['calificaciones'])
        suma_promedios += promedio_calificaciones
        contador += 1

if contador > 0:
    promedio_final = suma_promedios / contador
    print(f"\nEl promedio de calificaciones de los estudiantes con más de 18 años y edad primo es: {promedio_final:.2f}")
else:
    print("\nNo hay estudiantes con más de 18 años y edad primo.")