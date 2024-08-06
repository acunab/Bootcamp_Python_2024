// Mail

document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("meetingForm");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        event.stopPropagation();

        if (form.checkValidity() === false) {
            form.classList.add('was-validated');
        } else {
            var formData = new FormData(form);

            fetch('assets/php/procesar_formulario.php', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("Formulario enviado exitosamente!");
                    form.reset();
                    form.classList.remove('was-validated');
                } else {
                    alert("Hubo un error al enviar el formulario. Inténtalo nuevamente.");
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert("Hubo un error al enviar el formulario. Inténtalo nuevamente.");
            });
        }
    }, false);
});


// Modal Instances

const projects = [
    {id: 'modalProyecto1', title: 'Airex Concepción', images: ['assets/img/airex1.jpeg', 'assets/img/airex2.jpeg', 'assets/img/airex3.jpeg'], description: 'Airex Concepción deseaba actualizar su página web ya que la anterior no era responsiva ni sus productos estaban ordenados de acuerdo a sus líneas de negocio.'},
    {id: 'modalProyecto2', title: 'RRHH Universidad del Biobío', images: ['assets/img/ddhh1.jpeg', 'assets/img/ddhh2.jpeg', 'assets/img/ddhh3.jpeg'], description: 'Descripción detallada del proyecto 2.'},
    {id: 'modalProyecto3', title: 'Doctorado IA', images: ['assets/img/doctorado.jpeg'], description: 'Descripción detallada del proyecto 3.'},
    {id: 'modalProyecto4', title: 'Festival Desviaciones', images: ['assets/img/desv1.png', 'assets/img/desv2.png'], description: 'La web debía seguir la línea gráfica y colores que utiliza el festival, pero sin perder la estructura de una típica web de festival donde se muestran los datos de cada obra, actividades e información en los días del evento. Fue un proceso de diseño fluido y rápido.'},
    {id: 'modalProyecto5', title: 'Airex Concepción', images: ['assets/img/airex1.jpeg', 'assets/img/airex2.jpeg', 'assets/img/airex3.jpeg'], description: 'Airex Concepción deseaba actualizar su página web ya que la anterior no era responsiva ni sus productos estaban ordenados de acuerdo a sus líneas de negocio.'},
    {id: 'modalProyecto6', title: 'RRHH Universidad del Biobío', images: ['assets/img/ddhh1.jpeg', 'assets/img/ddhh2.jpeg', 'assets/img/ddhh3.jpeg'], description: 'Descripción detallada del proyecto 2.'},
    ];

projects.forEach(project => {
    const modalClone = document.querySelector('#modalTemplate').cloneNode(true);
    modalClone.id = project.id;
    modalClone.querySelector('.modal-title').textContent = project.title;
    const carouselId = 'carousel' + project.id;
    const carousel = modalClone.querySelector('#carouselTemplate');
    carousel.id = carouselId;
    modalClone.querySelector('.carousel-control-prev').setAttribute('data-bs-target', '#' + carouselId);
    modalClone.querySelector('.carousel-control-next').setAttribute('data-bs-target', '#' + carouselId);
    const carouselInner = modalClone.querySelector('.carousel-inner');
    carouselInner.innerHTML = '';
    project.images.forEach((image, index) => {
        const carouselItem = document.createElement('div');
        carouselItem.className = `carousel-item${index === 0 ? ' active' : ''}`;
        carouselItem.innerHTML = `<img src="${image}" class="d-block w-100" alt="...">`;
        carouselInner.appendChild(carouselItem);
    });
    
    modalClone.querySelector('.modal-body p').textContent = project.description;
    document.body.appendChild(modalClone);
});

