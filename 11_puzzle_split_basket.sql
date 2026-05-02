-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?"
\c view_lab

-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
SELECT order_id
FROM order_lines ol 
JOIN products p ON ol.prod_id = p.prod_id 
WHERE p.price < 15
INTERSECT
SELECT order_id
FROM order_lines ol 
JOIN products p ON ol.prod_id = p.prod_id 
WHERE p.price > 30;