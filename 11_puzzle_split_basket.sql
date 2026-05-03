-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?"
\c view_lab

-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
-- Connect to the database
\c view_lab

-- Find the order that contains both a <15 item and a >30 item
SELECT order_id
FROM order_lines ol
JOIN products p ON ol.prod_id = p.prod_id
GROUP BY order_id
HAVING COUNT(*) FILTER (WHERE p.price < 15) > 0
   AND COUNT(*) FILTER (WHERE p.price > 30) > 0;