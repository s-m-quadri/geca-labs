-- Task 6: EXISTS -- customers who have at least one order

<<<<<<< HEAD
-- TODO: SELECT c.name FROM customers c
--       WHERE EXISTS (
--         SELECT 1 FROM orders o WHERE o.cust_id = c.cust_id
--       );
=======
>>>>>>> d1e2bff (BT24F05F008)
SELECT c.name FROM customers c
WHERE EXISTS (
  SELECT 1 FROM orders o WHERE o.cust_id = c.cust_id
);