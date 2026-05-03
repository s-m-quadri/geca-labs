-- Task 3: Query the view (create it in 02 first)
-- Sum line_total per order_id
\c view_lab

-- TODO: SELECT order_id, SUM(line_total) AS order_total
--       FROM v_order_lines_detail
--       GROUP BY order_id;
-- Connect to the database
\c view_lab

-- Query the view to get the total revenue for each order
SELECT 
    order_id, 
    SUM(line_total) AS order_total
FROM v_order_lines_detail
GROUP BY order_id
ORDER BY order_id;