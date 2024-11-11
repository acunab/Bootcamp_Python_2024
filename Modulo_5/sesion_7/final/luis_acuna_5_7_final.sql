-- 1. Listar los clientes sin arriendos por medio de una subconsulta
SELECT c.RUT, c.Nombre
FROM Cliente c
WHERE c.RUT NOT IN (SELECT a.Cliente_RUT FROM Arriendo a);

-- 2. Listar todos los arriendos con las siguientes columnas: Folio, Fecha, Dias, ValorDia, NombreCliente, RutCliente
SELECT a.Folio, a.Fecha, a.Dias, a.ValorDia, c.Nombre AS NombreCliente, c.RUT AS RutCliente
FROM Arriendo a
JOIN Cliente c ON a.Cliente_RUT = c.RUT;

-- 3. Clasificar los clientes según la siguiente tabla
SELECT c.RUT, c.Nombre, 
       COUNT(a.Folio) AS CantidadArriendos,
       CASE 
           WHEN COUNT(a.Folio) BETWEEN 0 AND 1 THEN 'Bajo'
           WHEN COUNT(a.Folio) BETWEEN 2 AND 3 THEN 'Medio'
           ELSE 'Alto'
       END AS Clasificacion
FROM Cliente c
LEFT JOIN Arriendo a ON c.RUT = a.Cliente_RUT
GROUP BY c.RUT, c.Nombre;

-- 4. Por medio de una subconsulta, listar los clientes con el nombre de la herramienta más arrendada
SELECT DISTINCT c.RUT, c.Nombre, h.Nombre AS NombreHerramienta
FROM Cliente c
JOIN Arriendo a ON c.RUT = a.Cliente_RUT
JOIN Herramienta h ON a.Herramienta_IDHerramienta = h.IDHerramienta
WHERE a.Herramienta_IDHerramienta = (
    SELECT Herramienta_IDHerramienta
    FROM Arriendo
    GROUP BY Herramienta_IDHerramienta
    ORDER BY COUNT(*) DESC
    LIMIT 1
);