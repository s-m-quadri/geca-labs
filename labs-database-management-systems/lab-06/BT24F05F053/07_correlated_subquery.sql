-- Task 7: Correlated subquery -- customers who spent more than 50 total
-- (sum of qty * price across all their order lines)
\c view_lab

-- TODO: correlated pattern on customers + orders + order_lines + products
SELECT c.name
FROM customers c
WHERE (
	SELECT COALESCE(SUM(ol.qty * p.price), 0)
	FROM orders o
	JOIN order_lines ol ON ol.order_id = o.order_id
	JOIN products p ON p.prod_id = ol.prod_id
	WHERE o.cust_id = c.cust_id
) > 50
ORDER BY c.name;