-- Puzzle C (riddle)
-- "One order carried both a bargain-bin item (unit price under 15)
--  and a premium item (unit price over 30). Which order_id is it?"
\c view_lab

-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
SELECT ol.order_id
FROM view_lab.order_lines ol
JOIN view_lab.products p USING (prod_id)
GROUP BY ol.order_id
HAVING bool_or(p.price < 15)
    AND bool_or(p.price > 30);