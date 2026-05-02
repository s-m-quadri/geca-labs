-- Task 7: Correlated subquery — for each customer, show name only if they spent more than 50 total (sum qty*price across all lines)

USE view_lab;

SELECT c.name
FROM customers AS c
WHERE (
  SELECT COALESCE(SUM(ol.qty * p.price), 0)
  FROM orders AS o
  JOIN order_lines AS ol ON o.order_id = ol.order_id
  JOIN products AS p ON ol.prod_id = p.prod_id
  WHERE o.cust_id = c.cust_id
) > 50;
