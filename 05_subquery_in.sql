-- Task 5: IN subquery -- customers who ordered product id 20 (PenSet)
\c view_lab

USE view_lab;

SELECT name
FROM customers
WHERE cust_id IN (
  SELECT o.cust_id
  FROM orders o
  JOIN order_lines ol ON ol.order_id = o.order_id
  WHERE ol.prod_id = 20
);
