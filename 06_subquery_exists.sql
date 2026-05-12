\c view_lab
SELECT c.name
FROM customers AS c
WHERE EXISTS (
  SELECT 1 FROM orders AS o WHERE o.cust_id = c.cust_id
);