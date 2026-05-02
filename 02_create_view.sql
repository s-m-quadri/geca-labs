-- Task 2: Create a view v_order_lines_detail with line revenue
-- Columns: order_id, prod_id, qty, product name, unit price, line_total (qty * price)
\c view_lab

CREATE OR REPLACE VIEW v_order_lines_detail AS
SELECT 
    ol.order_id,
    ol.prod_id,
    ol.qty,
    p.product_name,
    p.unit_price,
    (ol.qty * p.unit_price) AS line_total
FROM order_lines ol
JOIN products p 
    ON ol.prod_id = p.prod_id;

-- TODO: CREATE OR REPLACE VIEW v_order_lines_detail AS
-- SELECT ...
