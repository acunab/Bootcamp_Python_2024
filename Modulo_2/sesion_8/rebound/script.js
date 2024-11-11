function mostrarMenu() {
    let opcion = 0;  // Inicializamos 'opcion' en 0 para entrar en el bucle
    while (opcion !== 5) {  // El bucle se repite mientras 'opcion' no sea 5
        opcion = parseInt(prompt(
            "Seleccione una opción:\n" +
            "1. Opción 1\n" +
            "2. Opción 2\n" +
            "3. Opción 3\n" +
            "4. Opción 4\n" +
            "5. Salir"
        ));
        
        switch (opcion) {
            case 1:
                alert("Has seleccionado la Opción 1, elige otra");
                break;
            case 2:
                alert("Has seleccionado la Opción 2, elige otra");
                break;
            case 3:
                alert("Has seleccionado la Opción 3, elige otra");
                break;
            case 4:
                alert("Has seleccionado la Opción 4, elige otra");
                break;
            case 5:
                alert("Salir");
                break;
            default:
                alert("Opción no válida, por favor seleccione una opción del 1 al 5");
        }
    }
}

// Llamar a la función para mostrar el menú cuando se carga la página
mostrarMenu();