--  and a premium item (unit price over 30). Which order_id is it?"
\c view_lab

-- TODO: HAVING with conditional sums, or EXISTS pair, or intersect of two subqueries
SELECT ol.order_id
FROM order_lines ol
JOIN products p ON ol.prod_id = p.prod_id
GROUP BY ol.order_id
HAVING
  BOOL_OR(p.price < 15) AND
  BOOL_OR(p.price > 30);
