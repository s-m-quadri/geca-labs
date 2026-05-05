-- Task 7: Correlated subquery -- customers who spent more than 50 total
-- (sum of qty * price across all their order lines)

SELECT c.name 
FROM customers c
WHERE 50 < (
  SELECT COALESCE(SUM(ol.qty * p.price), 0)
  FROM orders o
  JOIN order_lines ol ON o.order_id = ol.order_id
  JOIN products p ON ol.prod_id = p.prod_id
  WHERE o.cust_id = c.cust_id
);