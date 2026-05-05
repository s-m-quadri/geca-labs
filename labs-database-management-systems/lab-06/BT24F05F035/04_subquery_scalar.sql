-- Task 4: Scalar subquery -- products priced above the average product price
\c view_lab

SELECT name, price
FROM products
WHERE price > (
	SELECT AVG(price)
	FROM products
)
ORDER BY price, name;
