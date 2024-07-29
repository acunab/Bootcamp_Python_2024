console.log("calculadora")
alert("Hola, soy Eva, tu asistente virtual del servicio al Cliente de Mentel. Estoy aquí para: 1. Subtotal de productos, 2. Calcular el total iva, 3. COmpra con descuento e iva")
opcion = parseInt(prompt("Escribe el número de la opción deseada"));
var suma;
var precio1;
var cantprecio1;
var precio2;
var cantprecio2;
a = parseInt (prompt ("Introduce el primer número:"));
b = parseInt (prompt ("Introduce otro número:"));
    if (a ==0 && b ==0) {
        alert("Los númeero son 0, no se puede hacer operaciones")
    } else {
          
switch(opcion) {
    case 1:
        total = suma(a,b);
        alert("El resultado de la suma es " + total);
        break;
    case 2:
        total2= resta(a,b);
        alert("El resultado de la resta es " + total2);
        break;
    case 3:
        total4= division(a,b);
        alert("El resultado de la división es " + total4);
        break;
    default:
        alert("Opción no valida, leer correctamente las opciones");
        break;
}
}

alert("gracias por hacer uso de la calculadora");
//console.log(suma);

function suma(a,b){
    resultado=a + b;
    return resultado;
}
function resta(a,b){
    resultado=a - b;
    return resultado;
}
function multiplicacion(a,b){
    resultado=a * b;
    return resultado;
}
function division(a,b){
    
    if(a > b){
        resultado = a / b;
    }else{
        resultado=0;
    }
    
    return resultado;

}