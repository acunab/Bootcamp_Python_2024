console.log();

alert ("¿Qué número es mayor?")

// Declarar variables para los números usando var
var numero1;
var numero2;

// Solicitar el ingreso del primer número
numero1 = prompt("Ingrese el primer número");

// Solicitar el ingreso del segundo número
numero2 = prompt("Ingrese el segundo número");

// Comparar los números y mostrar el mensaje correspondiente
if (numero1 > numero2) {
    alert("El número " + numero1 + " es mayor que " + numero2);
} else if (numero2 > numero1) {
    alert("El número " + numero2 + " es mayor que " + numero1);
} else {
    alert("Ambos números son iguales");
}