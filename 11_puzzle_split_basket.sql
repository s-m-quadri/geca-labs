-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?"

<<<<<<< HEAD
-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
=======
>>>>>>> d1e2bff (BT24F05F008)
SELECT order_id
FROM order_lines ol 
JOIN products p ON ol.prod_id = p.prod_id 
WHERE p.price < 15
INTERSECT
SELECT order_id
FROM order_lines ol 
JOIN products p ON ol.prod_id = p.prod_id 
WHERE p.price > 30;