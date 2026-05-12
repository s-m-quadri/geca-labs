\c view_lab
SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products);