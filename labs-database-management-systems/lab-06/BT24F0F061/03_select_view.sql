-- Task 3: Query the view (create it in 02 first)
-- Sum line_total per order_id


-- TODO: SELECT order_id, SUM(line_total) AS order_total
--       FROM v_order_lines_detail
--       GROUP BY order_id;
select order_id, sum(line_total) as order_total
from v_order_lines_detail
group by order_id;
