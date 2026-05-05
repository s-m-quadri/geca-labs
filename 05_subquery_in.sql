-- Task 5: IN subquery -- customers who ordered product id 20 (PenSet)
\c view_lab

-- TODO: SELECT name FROM customers
--       WHERE cust_id IN (
--         SELECT cust_id FROM orders o
--         JOIN order_lines ol ON o.order_id = ol.order_id
--         WHERE ol.prod_id = 20
--       );
\c view_lab
SELECT c.name
FROM customers AS c
WHERE c.cust_id IN (
  SELECT o.cust_id
  FROM orders AS o
  JOIN order_lines AS ol ON ol.order_id = o.order_id
  WHERE ol.prod_id = 20
);
