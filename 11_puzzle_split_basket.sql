-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?"
USE view_lab;

-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
SELECT o.order_id
FROM orders o
JOIN order_lines ol ON o.order_id = ol.order_id
JOIN products p ON ol.prod_id = p.prod_id
GROUP BY o.order_id
HAVING SUM(CASE WHEN p.price < 15 THEN 1 ELSE 0 END) > 0
    AND SUM(CASE WHEN p.price > 30 THEN 1 ELSE 0 END) > 0;