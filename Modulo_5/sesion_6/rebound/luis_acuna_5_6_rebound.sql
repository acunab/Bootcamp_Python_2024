-- 1. Listar todos los vehículos que no han sido vendidos
SELECT *
FROM vehiculo
WHERE idVehiculo NOT IN (SELECT vehiculo_idVehiculo FROM venta);

-- 2. Listar todas las ventas de enero del 2020 con las columnas:
-- Folio, FechaVenta, MontoVenta, NombreCliente, RutCliente, Patente, NombreMarca, y Modelo
SELECT v.folio AS Folio,
       v.fecha AS FechaVenta,
       v.monto AS MontoVenta,
       c.nombre AS NombreCliente,
       c.rut AS RutCliente,
       ve.patente AS Patente,
       m.nombre AS NombreMarca,
       ve.modelo AS Modelo
FROM venta v
JOIN cliente c ON v.cliente_rut = c.rut
JOIN vehiculo ve ON v.vehiculo_idVehiculo = ve.idVehiculo
JOIN marca m ON ve.marca_idMarca = m.idMarca
WHERE v.fecha BETWEEN '2020-01-01' AND '2020-01-31';

-- 3. Sumar las ventas por mes y marca del año 2020
SELECT EXTRACT(MONTH FROM v.fecha) AS Mes,
       m.nombre AS Marca,
       SUM(v.monto) AS TotalVentas
FROM venta v
JOIN vehiculo ve ON v.vehiculo_idVehiculo = ve.idVehiculo
JOIN marca m ON ve.marca_idMarca = m.idMarca
WHERE EXTRACT(YEAR FROM v.fecha) = 2020
GROUP BY Mes, Marca
ORDER BY Mes, Marca;

-- 4. Listar Rut y Nombre de las tablas cliente y empresa
SELECT rut, nombre
FROM cliente
UNION ALL
SELECT rut, nombre
FROM empresa;