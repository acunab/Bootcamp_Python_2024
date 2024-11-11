const cliente = [
    {
        id: 1,
        nombre: "Luis",
        clave: "1234",
        saldo: 50000,         
    },
    {
        id: 1,
        nombre: "Luis",
        clave: "1234",
        saldo: 50000,         
    },
    {
        id: 1,
        nombre: "Luis",
        clave: "1234",
        saldo: 50000,         
    },
];

let idCliente = prompt("Ingresa el ID del cliente");
let passwordCliente = prompt("Ingresa la contraseña");

const login = clientes.find(
    (cliente) => cliente.id
)