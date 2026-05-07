-- Task 4: Scalar subquery -- products priced above the average product price
\c view_lab

-- TODO: SELECT name, price FROM products
--       WHERE price > ( ... scalar subquery for AVG(price) ... );
POSTGRESQL
SELECT prod_name, unit_price FROM products
WHERE unit_price > (SELECT AVG(unit_price) FROM products);  