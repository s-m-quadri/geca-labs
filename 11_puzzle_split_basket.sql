-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?"
\c view_lab

-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
SELECT order_id
FROM v_order_lines_detail
GROUP BY order_id
HAVING 
    COUNT(*) FILTER (WHERE unit_price < 15) > 0 
    AND 
    COUNT(*) FILTER (WHERE unit_price > 30) > 0;