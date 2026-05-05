SELECT * 
FROM (
    SELECT 
        ol.order_id, 
        SUM(ol.qty * p.price) AS rev
    FROM order_lines ol
    JOIN products p 
    ON ol.prod_id = p.prod_id
    GROUP BY ol.order_id
) AS t
WHERE t.rev > 30;