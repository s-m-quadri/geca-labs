-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15) and a premium item (unit price over 30).
--  Which order_id is it?"

USE view_lab;

SELECT ol.order_id
FROM order_lines AS ol
JOIN products AS p ON ol.prod_id = p.prod_id
GROUP BY ol.order_id
HAVING SUM(p.price < 15) > 0
   AND SUM(p.price > 30) > 0;
