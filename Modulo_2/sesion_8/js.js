var alumnos = ["Juan", "María", "Pedro", "Lucía", "Carlos"];
var calificaciones = {
    "Juan": [3],
    "María": [6],
    "Pedro": [2],
    "Lucía": [4],
    "Carlos": [5]
};
var promedios = {};

function verListaDeAlumnos() {
    console.log("Lista de Alumnos:");
    alumnos.forEach(alumno => {
        console.log(alumno);
    });
}

function verCalificacionesDeAlumnos() {
    console.log("Calificaciones de Alumnos:");
    for (var alumno in calificaciones) {
        console.log(alumno + ": " + calificaciones[alumno]);
        calificaciones[alumno].forEach(nota => {
            var estado = (nota >= 4) ? "Aprobado" : "Reprobado";
            console.log("Nota: " + nota + " - " + estado);
        });
    }
}

function calcularPromedioDelGrupo() {
    var totalNotas = 0;
    var totalCalificaciones = 0;

    for (var alumno in calificaciones) {
        var sumaNotas = calificaciones[alumno].reduce((a, b) => a + b, 0);
        var promedio = sumaNotas / calificaciones[alumno].length;
        promedios[alumno] = promedio;
        totalNotas += sumaNotas;
        totalCalificaciones += calificaciones[alumno].length;
    }

    var promedioGrupo = totalNotas / totalCalificaciones;
    console.log("El promedio del grupo es: " + promedioGrupo.toFixed(2));
}

function mostrarMenu() {
    var opcion;
    do {
        opcion = prompt("Menú:\n1. Ver lista de alumnos\n2. Ver calificaciones de alumnos\n3. Calcular el promedio del grupo\n4. Salir\nElige una opción:");
        opcion = parseInt(opcion);

        switch (opcion) {
            case 1:
                verListaDeAlumnos();
                break;
            case 2:
                verCalificacionesDeAlumnos();
                break;
            case 3:
                calcularPromedioDelGrupo();
                break;
            case 4:
                console.log("Saliendo...");
                break;
            default:
                console.log("Opción no válida. Intenta de nuevo.");
        }
    } while (opcion !== 4);
}

mostrarMenu();