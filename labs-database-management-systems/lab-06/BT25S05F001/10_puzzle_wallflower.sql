-- Puzzle B (riddle)
-- "Who never pressed checkout? List customer names with zero orders."

SELECT name 
FROM customers c
WHERE NOT EXISTS (
  SELECT 1 FROM orders o WHERE o.cust_id = c.cust_id
);