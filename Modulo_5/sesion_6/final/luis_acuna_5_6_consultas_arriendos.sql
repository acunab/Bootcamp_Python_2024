
-- Listar todos los arriendos con las columnas: Folio, Fecha, Días, ValorDia, NombreCliente, RutCliente
SELECT 
    A.Folio,
    A.Fecha,
    A.Dias,
    A.ValorDia,
    C.Nombre AS NombreCliente,
    C.RUT AS RutCliente
FROM 
    Arriendo A
JOIN 
    Cliente C ON A.Cliente_RUT = C.RUT;

-- Listar los clientes sin arriendos
SELECT 
    C.RUT,
    C.Nombre
FROM 
    Cliente C
LEFT JOIN 
    Arriendo A ON C.RUT = A.Cliente_RUT
WHERE 
    A.Folio IS NULL;

-- Listar RUT y Nombre de las tablas Empresa y Cliente

-- Para la tabla Empresa
SELECT 
    RUT,
    Nombre
FROM 
    Empresa;

-- Para la tabla Cliente
SELECT 
    RUT,
    Nombre
FROM 
    Cliente;

-- Listar la cantidad de arriendos por mes
SELECT 
    EXTRACT(YEAR FROM Fecha) AS Año,
    EXTRACT(MONTH FROM Fecha) AS Mes,
    COUNT(*) AS CantidadArriendos
FROM 
    Arriendo
GROUP BY 
    EXTRACT(YEAR FROM Fecha),
    EXTRACT(MONTH FROM Fecha)
ORDER BY 
    Año,
    Mes;
