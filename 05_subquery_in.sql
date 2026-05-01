-- Task 5: IN subquery -- customers who ordered product id 20 (PenSet)
\c view_lab

SELECT name
FROM customers
WHERE cust_id IN (
	SELECT o.cust_id
	FROM orders AS o
	JOIN order_lines AS ol ON ol.order_id = o.order_id
	WHERE ol.prod_id = 20
);
