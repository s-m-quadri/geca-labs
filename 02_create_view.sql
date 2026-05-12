\c view_lab
CREATE OR REPLACE VIEW v_order_lines_detail AS
SELECT
  ol.order_id,
  ol.prod_id,
  ol.qty,
  p.name               AS product_name,
  p.price              AS unit_price,
  ol.qty * p.price     AS line_total
FROM order_lines AS ol
JOIN products    AS p ON p.prod_id = ol.prod_id;