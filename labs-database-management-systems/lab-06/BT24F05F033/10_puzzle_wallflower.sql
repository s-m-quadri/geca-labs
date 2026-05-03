-- Puzzle B (riddle)
-- "Who never pressed checkout? List customer names with zero orders."
\c view_lab

SELECT name FROM customers
WHERE cust_id NOT IN (SELECT cust_id FROM orders);
