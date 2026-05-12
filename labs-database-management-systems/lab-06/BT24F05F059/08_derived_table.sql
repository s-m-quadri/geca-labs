\c view_lab
SELECT order_id, rev
FROM (
  SELECT ol.order_id, SUM(ol.qty * p.price) AS rev
  FROM order_lines AS ol
  JOIN products    AS p ON p.prod_id = ol.prod_id
  GROUP BY ol.order_id
) AS t
WHERE t.rev > 30;