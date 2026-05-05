-- List all products with supplier names
SELECT p.name, s.name AS supplier
FROM product p
JOIN supplier s ON p.supplier_id = s.supplier_id;

-- Total quantity sold per product
SELECT p.name, SUM(od.quantity) AS total_sold
FROM order_details od
JOIN product p ON od.product_id = p.product_id
GROUP BY p.name;

-- Products sold more than 1 unit
SELECT p.name, SUM(od.quantity) AS total
FROM order_details od
JOIN product p ON p.product_id = od.product_id
GROUP BY p.name
HAVING SUM(od.quantity) > 1;

-- Products with stock less than average stock
SELECT name FROM product
WHERE product_id IN (
  SELECT product_id FROM inventory
  WHERE quantity < (SELECT AVG(quantity) FROM inventory)
);

-- Which products are low in stock (less than 10)?
SELECT p.name, i.quantity
FROM product p
JOIN inventory i ON p.product_id = i.product_id
WHERE i.quantity < 10;

CREATE VIEW sales_summary AS
SELECT p.name, SUM(od.quantity) AS total_sales
FROM order_details od
JOIN product p ON p.product_id = od.product_id
GROUP BY p.name;

-- Use view
SELECT * FROM sales_summary;

SELECT SUM(p.price * od.quantity) AS total_revenue
FROM order_details od
JOIN product p ON p.product_id = od.product_id;


SELECT p.name, SUM(od.quantity) AS total
FROM order_details od
JOIN product p ON p.product_id = od.product_id
GROUP BY p.name
ORDER BY total DESC
LIMIT 1;