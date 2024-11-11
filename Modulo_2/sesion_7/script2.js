alert ("bienvenidos a la calculadora")
console.log("calculadora")
alert("Opciones: 1. Suma, 2. Resta, 3. Multiplicación, 4. División")
opcion = parseInt(prompt("Escribe el número de la opción deseada"));
var suma;
var a;
var b;
a = parseInt (prompt ("Introduce el primer número:"));
b = parseInt (prompt ("Introduce otro número:"));
    if (a ==0 && bb ==0) {
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
        total3= multiplicacion(a,b);
        alert("El resultado de la multiplicación es " + total3);
        break;
    case 4:
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