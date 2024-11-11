var num_articulos = parseInt(prompt("número de artículos que desea comprar"))
//ciclo for
for(var inicio=1; inicio<=num_articulos; inicio++){
    var precio_articulo= parseInt(prompt("Dame precio de artículo" + inicio))
    var cantidad_articulo= parseInt(prompt("Dame cantidad" + inicio))

    console.log("producto" + precio_articulo);
    console.log("Cantidad a " + cantidad_articulo);
    console.log("el subtotal es = " + calcular_subtotal(precio_articulo,num_articulos
    ));
}
// ciclo do while

function calcular_subtotal(precio,cantidad){
    subtotal= (precio * cantidad) *1.19;
    return subtotal;
}