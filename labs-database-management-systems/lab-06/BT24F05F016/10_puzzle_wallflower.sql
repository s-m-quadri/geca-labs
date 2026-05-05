-- Puzzle B (riddle)
-- "Who never pressed checkout? List customer names with zero orders."
\c view_lab

-- TODO: anti-join or NOT EXISTS
\c view_lab
-- Option A: NOT EXISTS
SELECT name FROM customers AS c
WHERE NOT EXISTS (
  SELECT 1 FROM orders AS o WHERE o.cust_id = c.cust_id
);
 
-- Option B: LEFT JOIN anti-join
SELECT c.name
FROM customers AS c
LEFT JOIN orders AS o ON o.cust_id = c.cust_id
WHERE o.order_id IS NULL;