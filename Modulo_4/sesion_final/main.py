# main.py

from vehiculo import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta
import csv

def guardar_datos_csv(vehiculos, nombre_archivo="vehiculos.csv"):
    with open(nombre_archivo, "w", newline='') as archivo:
        archivo_csv = csv.writer(archivo)
        for vehiculo in vehiculos:
            # Guardamos el tipo de clase como texto y los atributos como un diccionario
            archivo_csv.writerow([vehiculo.__class__.__name__, vehiculo.__dict__])

def leer_datos_csv(nombre_archivo="vehiculos.csv"):
    vehiculos = {"Particular": [], "Carga": [], "Bicicleta": [], "Motocicleta": []}
    with open(nombre_archivo, "r") as archivo:
        archivo_csv = csv.reader(archivo)
        for fila in archivo_csv:
            tipo = fila[0]
            atributos = eval(fila[1])
            if tipo == "Particular":
                vehiculo = Particular(**atributos)
            elif tipo == "Carga":
                vehiculo = Carga(**atributos)
            elif tipo == "Bicicleta":
                vehiculo = Bicicleta(**atributos)
            elif tipo == "Motocicleta":
                vehiculo = Motocicleta(**atributos)
            else:
                continue
            vehiculos[tipo].append(vehiculo)
    return vehiculos

if __name__ == "__main__":
    # Creación de instancias de ejemplo
    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehiculos = [particular, carga, bicicleta, motocicleta]
    guardar_datos_csv(vehiculos)
    
    # Lectura de datos desde el CSV
    datos_leidos = leer_datos_csv()

    # Impresión de datos clasificados
    for tipo, datos in datos_leidos.items():
        print(f"\nLista de Vehiculos {tipo}")
        for dato in datos:
            print(dato)

    # Verificación de instancias
    print("\nVerificación de instancias:")
    print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
    print("Motocicleta es instancia con relación a Automovil:", isinstance(motocicleta, Automovil))
    print("Motocicleta es instancia con relación a Particular:", isinstance(motocicleta, Particular))
    print("Motocicleta es instancia con relación a Carga:", isinstance(motocicleta, Carga))
    print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
    print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))