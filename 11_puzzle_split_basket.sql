-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?"
\c view_lab

-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
SELECT o.order_id
FROM orders o
WHERE EXISTS (
    SELECT 1
    FROM order_lines ol
    JOIN products p ON ol.prod_id = p.prod_id
    WHERE ol.order_id = o.order_id AND p.price < 15
)
AND EXISTS (
    SELECT 1
    FROM order_lines ol
    JOIN products p ON ol.prod_id = p.prod_id
    WHERE ol.order_id = o.order_id AND p.price > 30
);