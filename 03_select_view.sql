\c view_lab
SELECT order_id, SUM(line_total) AS order_revenue
FROM v_order_lines_detail
GROUP BY order_id
ORDER BY order_id;