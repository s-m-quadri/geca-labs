-- Task 6: EXISTS -- customers who have at least one order
\c view_lab

-- TODO: SELECT c.name FROM customers c
--       WHERE EXISTS (
--         SELECT 1 FROM orders o WHERE o.cust_id = c.cust_id
--       );
SELECT c.name FROM customers c
WHERE EXISTS (
  SELECT 1 FROM orders o WHERE o.cust_id = c.cust_id
);      