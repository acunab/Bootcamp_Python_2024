
-- 1. Listar los clientes sin ventas por medio de una subconsulta
SELECT RUT, Nombre, Correo, Direccion, Celular
FROM Cliente
WHERE RUT NOT IN (SELECT Cliente_RUT FROM Venta);

-- 2. Listar todas las ventas con las columnas: Folio, Fecha, Monto, NombreCliente, RutCliente
SELECT v.Folio, v.Fecha, v.Monto, c.Nombre AS NombreCliente, c.RUT AS RutCliente
FROM Venta v
JOIN Cliente c ON v.Cliente_RUT = c.RUT;

-- 3. Clasificar los clientes según la tabla proporcionada
SELECT c.RUT, c.Nombre, SUM(v.Monto) AS TotalVentas,
       CASE
           WHEN SUM(v.Monto) BETWEEN 0 AND 1000000 THEN 'Standar'
           WHEN SUM(v.Monto) BETWEEN 1000001 AND 3000000 THEN 'Gold'
           WHEN SUM(v.Monto) > 3000000 THEN 'Premium'
       END AS Clasificacion
FROM Cliente c
LEFT JOIN Venta v ON c.RUT = v.Cliente_RUT
GROUP BY c.RUT, c.Nombre;

-- 4. Listar las ventas con la marca del vehículo más vendido utilizando una subconsulta
SELECT v.Folio, v.Fecha, v.Monto, m.Nombre AS MarcaVehiculo
FROM Venta v
JOIN Vehiculo vh ON v.Vehiculo_IDVehiculo = vh.IDVehiculo
JOIN Marca m ON vh.Marca_IDMarca = m.IDMarca
WHERE vh.Marca_IDMarca = (
       SELECT Marca_IDMarca
       FROM Vehiculo
       GROUP BY Marca_IDMarca
       ORDER BY COUNT(*) DESC
       FETCH FIRST 1 ROWS ONLY
);
