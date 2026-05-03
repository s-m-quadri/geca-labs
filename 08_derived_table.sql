-- Task 8: Derived table in FROM
-- From a subquery that computes per-order revenue, select orders where revenue > 30
\c view_lab

USE view_lab;

SELECT t.order_id, t.rev
FROM (
  SELECT ol.order_id, SUM(ol.qty * p.price) AS rev
  FROM order_lines ol
  JOIN products p ON p.prod_id = ol.prod_id
  GROUP BY ol.order_id
) AS t
WHERE t.rev > 30;
