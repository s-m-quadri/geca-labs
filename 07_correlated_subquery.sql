SELECT c.name
FROM customers c
WHERE (
    SELECT SUM(ol.qty * p.price)
    FROM orders o
    JOIN order_lines ol ON o.order_id = ol.order_id
    JOIN products p ON ol.prod_id = p.prod_id
    WHERE o.cust_id = c.cust_id
) > 50;