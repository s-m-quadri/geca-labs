\c view_lab
SELECT c.name
FROM customers AS c
WHERE c.cust_id IN (
  SELECT o.cust_id
  FROM orders AS o
  JOIN order_lines AS ol ON ol.order_id = o.order_id
  WHERE ol.prod_id = 20
);