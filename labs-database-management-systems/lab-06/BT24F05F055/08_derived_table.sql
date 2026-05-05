-- Task 8: Derived table in FROM
-- From a subquery that computes per-order revenue, select orders where revenue > 30
\c view_lab

SELECT *
FROM (
	SELECT ol.order_id, SUM(ol.qty * p.price) AS rev
	FROM order_lines AS ol
	JOIN products AS p ON p.prod_id = ol.prod_id
	GROUP BY ol.order_id
) AS t
WHERE t.rev > 30;
