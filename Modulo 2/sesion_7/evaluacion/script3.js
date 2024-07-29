function mostrarMenu() {
    var opcion = prompt(
        "Hola, soy Eva, tu asistente virtual del servicio al Cliente de Mentel. Estoy aquí para ayudarte en lo que necesites.:\n" +
        "Por favor, elija una opción:\n" +
        "1. Boletas y Pagos\n" +
        "2. Señal y Llamada\n" +
        "3. Oferta Comercial\n" +
        "4. Otras Consultas"
    );

    switch (opcion) {
        case '1':
            boletasYPagos();
            break;
        case '2':
            senalYLlamada();
            break;
        case '3':
            ofertaComercial();
            break;
        case '4':
            otrasConsultas();
            break;
        default:
            alert("Opción no válida, Gracias por preferir nuestros servicios.");
            break;
    }
}
function boletasYPagos() {
    var subopcion = prompt(
        "Ha seleccionado Boletas y Pagos.\n" +
        "Por favor, elija una opción:\n" +
        "1. Ver boleta\n" +
        "2. Pagar cuenta"
    );

    if (subopcion === '1') {
        alert("Haga click para descargar su boleta");
    } else if (subopcion === '2') {
        alert("Usted está siendo transferido. Espere por favor..");
    } else {
        alert("Opción no válida, Gracias por preferir nuestros servicios.");
    }
}

function senalYLlamada() {
    var subopcion = prompt(
        "Ha seleccionado Señal y llamadas.\n" +
        "Por favor, elija una opción:\n" +
        "1. Problemas con la señal\n" +
        "2. Problemas con las llamadas"
    );

    if (subopcion === '1') {
        prompt("A continuación escriba su solicitud");
    } else if (subopcion === '2') {
        prompt("A continuación escriba su solicitud");
    } else {
        alert("Estimado usuario, su solicitud: 'Tengo problemas... ha sido ingresada con éxito. Pronto será contactado por alguien de nuestra empresa.'");
    }
}

function ofertaComercial() {
    var subopcion = prompt(
        "¡Mentel tiene una oferta comercial acorde a tus necesidades!\n" +
        "Para conocere más información y recibir asesoría escribe SI para llamarte. De lo contrario escribe NO"
    );

    if (subopcion === 'SI') {
        alert("Nos contactaremos contigo enseguida.");
    } else if (subopcion === 'NO') {
        alert("Gracias por preferirnos");
    } else {
        alert("Opción invalida. Gracias por preferirnos'");
    }
}

function otrasConsultas() {
    prompt(
        "Ingresa tu consulta"
    );
    alert("Su consulta fue ingresada con éxito.");
    
}

window.onload = function() {
    mostrarMenu();
}