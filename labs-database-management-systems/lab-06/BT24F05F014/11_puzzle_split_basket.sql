-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?

-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
USE view_lab;
SELECT order_id
FROM v_order_lines_detail
GROUP BY order_id
HAVING
    SUM(CASE WHEN unit_price < 15 THEN 1 ELSE 0 END) > 0
    AND
    SUM(CASE WHEN unit_price > 30 THEN 1 ELSE 0 END) > 0;

