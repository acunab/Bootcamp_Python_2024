class SistemaCalificaciones {
    constructor() {
        this.alumnos = ["Alumno1", "Alumno2", "Alumno3", "Alumno4", "Alumno5", "Alumno6"];
        this.calificaciones = {
            "Alumno1": [5, 6, 7],
            "Alumno2": [3, 4, 2],
            "Alumno3": [6, 7, 5],
            "Alumno4": [2, 3, 4],
            "Alumno5": [7, 6, 6],
            "Alumno6": [4, 5, 6]
        };
    }

    mostrarMenu() {
        let opcion;
        do {
            opcion = prompt("Menu:\n1. Ver lista de alumnos\n2. Ver calificaciones de alumnos\n3. Calcular el promedio de todo el grupo\n4. Salir\nElige una opción: ");
            switch(opcion) {
                case "1":
                    this.verListaDeAlumnos();
                    break;
                case "2":
                    this.verCalificacionesDeAlumnos();
                    break;
                case "3":
                    this.calcularPromedioDelGrupo();
                    break;
                case "4":
                    alert("Saliendo del sistema...");
                    break;
                default:
                    alert("Opción no válida");
            }
        } while(opcion !== "4");
    }

    verListaDeAlumnos() {
        let lista = "Lista de alumnos:\n";
        this.alumnos.forEach(alumno => {
            lista += `${alumno}\n`;
        });
        alert(lista);
    }

    verCalificacionesDeAlumnos() {
        let calificacionesTexto = "Calificaciones de alumnos:\n";
        for (let alumno in this.calificaciones) {
            let calificaciones = this.calificaciones[alumno];
            let estado = calificaciones.map(calificacion => {
                return calificacion >= 4 ? "Aprobado" : "Reprobado";
            });
            calificacionesTexto += `${alumno}: ${calificaciones.join(", ")} (${estado.join(", ")})\n`;
        }
        alert(calificacionesTexto);
    }

    calcularPromedioDelGrupo() {
        let totalCalificaciones = 0;
        let numeroCalificaciones = 0;
        for (let alumno in this.calificaciones) {
            this.calificaciones[alumno].forEach(calificacion => {
                totalCalificaciones += calificacion;
                numeroCalificaciones++;
            });
        }
        let promedio = totalCalificaciones / numeroCalificaciones;
        alert(`El promedio del grupo es: ${promedio.toFixed(2)}`);
    }
}

const sistema = new SistemaCalificaciones();
sistema.mostrarMenu();