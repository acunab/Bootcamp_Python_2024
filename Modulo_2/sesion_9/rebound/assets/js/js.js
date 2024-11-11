// Selección de elementos
const text1 = document.getElementById('text1');
const text2 = document.getElementById('text2');
const img = document.getElementById('img');
const caja3 = document.getElementById('caja3');

// Mostrar text2 al pasar el mouse por text1
text1.addEventListener('mouseenter', () => {
  text2.style.display = 'block';
});

// Ocultar text2 al salir del mouse de text1
text1.addEventListener('mouseleave', () => {
  text2.style.display = 'none';
});

// Agrandar imagen al hacer clic en caja2
document.getElementById('caja2').addEventListener('click', () => {
  img.style.width = '100%';
});

// Volver al tamaño original al salir el mouse de caja2
document.getElementById('caja2').addEventListener('mouseleave', () => {
  img.style.width = '20%';
});

// Agrandar el texto en caja3 al hacer doble clic
caja3.addEventListener('dblclick', () => {
  caja3.style.fontSize = '2em'; // Agranda la fuente
});