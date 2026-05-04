SELECT name 
FROM customers
WHERE cust_id IN (
    SELECT o.cust_id 
    FROM orders o
    JOIN order_lines ol 
    ON o.order_id = ol.order_id
    WHERE ol.prod_id = 20
);