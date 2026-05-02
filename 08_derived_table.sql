-- Task 8: Derived table in FROM — from a subquery that computes per-order revenue, select orders where revenue > 30

USE view_lab;

-- TODO: SELECT ... FROM ( SELECT order_id, SUM(qty * price) AS rev FROM order_lines JOIN products ... GROUP BY order_id ) AS t WHERE t.rev > 30;
SELECT t.order_id, t.rev
FROM (
  SELECT ol.order_id, SUM(ol.qty * p.price) AS rev
  FROM order_lines ol
  JOIN products p ON ol.prod_id = p.prod_id
  GROUP BY ol.order_id
) AS t
WHERE t.rev > 30;