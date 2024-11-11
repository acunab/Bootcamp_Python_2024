
-- Consultas para insertar, modificar y eliminar en Customer, Staff y Actor

-- Insertar un Customer
INSERT INTO customer (store_id, first_name, last_name, email, address_id, activebool, create_date)
VALUES (1, 'John', 'Doe', 'john.doe@example.com', 5, true, CURRENT_DATE);

-- Modificar un Customer
UPDATE customer
SET email = 'john.newemail@example.com'
WHERE customer_id = 1;

-- Eliminar un Customer
DELETE FROM customer
WHERE customer_id = 1;

-- Insertar un Staff
INSERT INTO staff (first_name, last_name, address_id, email, store_id, username, password, active)
VALUES ('Jane', 'Smith', 5, 'jane.smith@example.com', 1, 'jsmith', 'password123', true);

-- Modificar un Staff
UPDATE staff
SET email = 'jane.newemail@example.com'
WHERE staff_id = 1;

-- Eliminar un Staff
DELETE FROM staff
WHERE staff_id = 1;

-- Insertar un Actor
INSERT INTO actor (first_name, last_name)
VALUES ('Robert', 'Downey');

-- Modificar un Actor
UPDATE actor
SET last_name = 'Downey Jr.'
WHERE actor_id = 1;

-- Eliminar un Actor
DELETE FROM actor
WHERE actor_id = 1;

-- Listar todas las rentals con los datos del customer dado un año y mes
SELECT rental.*, customer.first_name, customer.last_name
FROM rental
JOIN customer ON rental.customer_id = customer.customer_id
WHERE EXTRACT(YEAR FROM rental_date) = 2023 AND EXTRACT(MONTH FROM rental_date) = 7;

-- Listar Número, Fecha (payment_date) y Total (amount) de todas las payments
SELECT payment_id AS "Número", payment_date AS "Fecha", amount AS "Total"
FROM payment;

-- Listar todas las films del año 2006 que contengan un rental_rate mayor a 4.0
SELECT *
FROM film
WHERE release_year = 2006 AND rental_rate > 4.0;
