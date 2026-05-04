SELECT ol.order_id
FROM order_lines ol
JOIN products p 
ON ol.prod_id = p.prod_id
GROUP BY ol.order_id
HAVING 
    SUM(CASE WHEN p.price < 15 THEN 1 ELSE 0 END) > 0
AND SUM(CASE WHEN p.price > 30 THEN 1 ELSE 0 END) > 0;