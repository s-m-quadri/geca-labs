-- Task 2: Create a view v_order_lines_detail with line revenue
-- Columns: order_id, prod_id, qty, product name, unit price, line_total (qty * price)


-- TODO: CREATE OR REPLACE VIEW v_order_lines_detail AS
-- SELECT ...
create or replace view v_order_lines_detail as
select ol.order_id, ol.prod_id, ol.qty, p.name as product_name, p.price as unit_price, ol.qty * p.price as line_total
from order_lines ol
join products p on ol.prod_id = p.prod_id;
