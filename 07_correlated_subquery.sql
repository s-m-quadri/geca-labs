-- Task 7: Correlated subquery — for each customer, show name only if they spent more than 50 total (sum qty*price across all lines)

USE view_lab;

-- TODO: correlated pattern on customers + orders + order_lines + products

SELECT name
FROM customers c
WHERE (
    SELECT SUM(ol.qty * p.price)
    FROM orders o
    JOIN order_lines ol ON o.order_id = ol.order_id
    JOIN products p ON ol.prod_id = p.prod_id
    WHERE o.cust_id = c.cust_id
) > 50;