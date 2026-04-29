-- Task 7: Correlated subquery -- customers who spent more than 50 total
-- (sum of qty * price across all their order lines)
\c view_lab


SELECT 
    c.customer_id, 
    c.customer_name -- or other relevant customer columns
FROM customers c
WHERE (
    SELECT SUM(ol.quantity * p.price)
    FROM orders o
    JOIN order_lines ol ON o.order_id = ol.order_id
    JOIN products p ON ol.product_id = p.product_id
    WHERE o.customer_id = c.customer_id
) > 50;
