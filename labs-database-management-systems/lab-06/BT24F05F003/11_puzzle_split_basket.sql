-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?"
\c view_lab

-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
SELECT order_id
FROM order_lines ol
JOIN products p ON ol.prod_id = p.prod_id
GROUP BY order_id
HAVING SUM(CASE WHEN p.price < 15 THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN p.price > 30 THEN 1 ELSE 0 END) > 0;   