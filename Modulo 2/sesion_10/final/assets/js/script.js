$(document).ready(function() {
  // Cuando se haga clic en "Ver más"
  $(".text-body-secondary").click(function() {
      // Obtener el id del botón clicado
      var idBoton = $(this).attr("id");
      // Mostrar u ocultar la sección de detalles correspondiente al botón clicado
      $("#detalles" + idBoton).toggle();
  });

  // Cuando se haga clic en el botón de cierre (X)
  $(".btn-close").click(function() {
      // Ocultar la sección de detalles que está abierta
      $(this).closest(".detalles").hide();
  });
});