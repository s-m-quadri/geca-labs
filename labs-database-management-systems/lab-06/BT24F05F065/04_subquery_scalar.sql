-- Task 4: Scalar subquery -- products priced above the average product price

-- TODO: SELECT name, price FROM products
--       WHERE price > ( ... scalar subquery for AVG(price) ... );

SELECT name, price 
FROM products
WHERE price > (SELECT AVG(price) FROM products);