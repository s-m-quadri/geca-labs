-- Task 7: Correlated subquery -- customers who spent more than 50 total
-- (sum of qty * price across all their order lines)
\c view_lab

-- TODO: correlated pattern on customers + orders + order_lines + products
SELECT c.cust_name 
FROM customers c
WHERE (
    SELECT SUM(ol.qty * p.price)
    FROM orders o
    JOIN order_lines ol ON o.order_id = ol.order_id
    JOIN products p ON ol.prod_id = p.prod_id
    WHERE o.cust_id = c.cust_id  -- This correlation links the subquery to the outer row
) > 50;