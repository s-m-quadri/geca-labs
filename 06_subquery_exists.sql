-- Task 6: EXISTS -- customers who have at least one order
\c view_lab

-- TODO: SELECT c.name FROM customers c
--       WHERE EXISTS (
--         SELECT 1 FROM orders o WHERE o.cust_id = c.cust_id
--       );
-- Connect to the database
\c view_lab

-- Find customers who have placed at least one order
SELECT c.name 
FROM customers c
WHERE EXISTS (
    SELECT 1 
    FROM orders o 
    WHERE o.cust_id = c.cust_id
);