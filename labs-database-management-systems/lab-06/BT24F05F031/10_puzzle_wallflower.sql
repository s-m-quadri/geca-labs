-- Puzzle B (riddle)
-- "Who never pressed checkout? List customer names with zero orders."
\c view_lab

-- TODO: anti-join or NOT EXISTS
SELECT 
  c.name
FROM customers c
WHERE NOT EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.cust_id = c.cust_id
);
