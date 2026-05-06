-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?"
\c view_lab

SELECT order_id
FROM order_lines ol
JOIN products p ON ol.prod_id = p.prod_id
GROUP BY order_id
HAVING COUNT(CASE WHEN p.price < 15 THEN 1 END) > 0
   AND COUNT(CASE WHEN p.price > 30 THEN 1 END) > 0;
