-- \c view_lab

CREATE OR REPLACE VIEW v_order_lines_detail AS
SELECT 
    ol.order_id, 
    ol.prod_id, 
    ol.qty, 
    p.prod_name, 
    p.price AS unit_price, 
    (ol.qty * p.price) AS line_total
FROM order_lines ol
JOIN products p ON ol.prod_id = p.prod_id;

-- Verify the view creation
SELECT * FROM v_order_lines_detail LIMIT 10;
