// Array inicial de tareas
var tareas = [
    { tarea: "Pintar la fachada de la casa" },
    { tarea: "Comprar comida para el perro" },
    { tarea: "Pagar la tarjeta de crédito" }
];

// Función para actualizar la tabla de tareas
function actualizarTabla() {
    const cuerpoTabla = document.getElementById('cuerpo-tabla');
    cuerpoTabla.innerHTML = '';

    tareas.forEach((item, index) => {
        const fila = document.createElement('tr');

        const celdaTarea = document.createElement('td');
        celdaTarea.textContent = item.tarea;
        fila.appendChild(celdaTarea);

        const celdaBoton = document.createElement('td');
        const botonFinalizar = document.createElement('button');
        botonFinalizar.textContent = 'Finalizar';
        botonFinalizar.classList.add('btn', 'btn-danger');
        botonFinalizar.addEventListener('click', function() {
            eliminarTarea(index);
        });
        celdaBoton.appendChild(botonFinalizar);
        fila.appendChild(celdaBoton);

        cuerpoTabla.appendChild(fila);
    });
}

// Función para eliminar una tarea de la lista
function eliminarTarea(indice) {
    tareas.splice(indice, 1);
    actualizarTabla();
}

// Función para agregar una nueva tarea a la lista
function agregarTarea() {
    const inputTarea = document.getElementById('nuevaTarea');
    const nuevaTareaTexto = inputTarea.value.trim();

    if (nuevaTareaTexto !== '') {
        tareas.push({ tarea: nuevaTareaTexto });
        inputTarea.value = '';
        actualizarTabla();
        toggleFormulario();
    }
}

// Función para mostrar/ocultar el formulario de agregar tarea
function toggleFormulario() {
    const formulario = document.getElementById('formulario');
    formulario.style.display = formulario.style.display === 'none' || formulario.style.display === '' ? 'block' : 'none';
}

// Evento para el botón de agregar tarea
document.querySelector('.btn-success').addEventListener('click', toggleFormulario);

// Evento para el botón de agregar del formulario
document.querySelector('.btn-primary').addEventListener('click', agregarTarea);

// Inicializar la tabla con las tareas existentes
document.addEventListener('DOMContentLoaded', actualizarTabla);