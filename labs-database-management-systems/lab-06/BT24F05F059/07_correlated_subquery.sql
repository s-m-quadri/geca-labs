\c view_lab
SELECT c.name
FROM customers AS c
WHERE (
  SELECT COALESCE(SUM(ol.qty * p.price), 0)
  FROM orders AS o
  JOIN order_lines AS ol ON ol.order_id = o.order_id
  JOIN products    AS p  ON p.prod_id   = ol.prod_id
  WHERE o.cust_id = c.cust_id
) > 50;