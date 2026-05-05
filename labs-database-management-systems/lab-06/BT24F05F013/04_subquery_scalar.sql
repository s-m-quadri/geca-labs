-- Task 4: Scalar subquery -- products priced above the average product price
USE view_lab;

-- TODO: SELECT name, price FROM products
--       WHERE price > ( ... scalar subquery for AVG(price) ... );
USE view_lab;

SELECT 
    name, 
    price 
FROM products
WHERE price > (
    SELECT AVG(price) 
    FROM products
);