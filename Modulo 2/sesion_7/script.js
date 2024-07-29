alert ("bienvenidos a la calculadora")
console.log("calculadora")
var suma;
var a = 6
var b = 8
a = parseInt (prompt ("Introduce el primer número:"));
b = parseInt (prompt ("Introduce otro número:"));
total = suma(a,b);
alert("El resultado de la suma es " + total);
total2= resta(a,b);
alert("El resultado de la resta es " + total2);
total3= multiplicacion(a,b);
alert("El resultado de la multiplicación es " + total3);
total4= division(a,b);
alert("El resultado de la división es " + total4);
//var a = prompt ("Introduce el primer número:");
//var b = prompt ("Introduce el primer número:");
// Convierte las entradas a números
//var suma = parseFloat(a) + parseFloat(b);
// Muestra el resultado en una alerta
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