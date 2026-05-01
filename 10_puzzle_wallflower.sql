-- Puzzle B (riddle)
-- "Who never pressed checkout? List customer names with zero orders."
\c view_lab

SELECT c.name
FROM customers AS c
WHERE NOT EXISTS (
	SELECT 1
	FROM orders AS o
	WHERE o.cust_id = c.cust_id
);
