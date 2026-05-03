-- Task 8: Derived table in FROM
-- From a subquery that computes per-order revenue, select orders where revenue > 30
\c view_lab

-- TODO: SELECT * FROM (
--   SELECT order_id, SUM(ol.qty * p.price) AS rev
--   FROM order_lines ol
--   JOIN products p ON ol.prod_id = p.prod_id
--   GROUP BY order_id
-- ) AS t
-- WHERE t.rev > 30;
-- Connect to the database
\c view_lab

-- Use a derived table to filter orders with revenue greater than 30
SELECT * FROM (
    SELECT 
        ol.order_id, 
        SUM(ol.qty * p.price) AS rev
    FROM order_lines ol
    JOIN products p ON ol.prod_id = p.prod_id
    GROUP BY order_id
) AS t
WHERE t.rev > 30;