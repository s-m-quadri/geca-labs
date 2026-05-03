-- Task 4: Scalar subquery -- products priced above the average product price
\c view_lab

-- TODO: SELECT name, price FROM products
--       WHERE price > ( ... scalar subquery for AVG(price) ... );
-- Connect to the database
\c view_lab

-- Find products priced above the average
SELECT 
    name, 
    price 
FROM products
WHERE price > (SELECT AVG(price) FROM products);