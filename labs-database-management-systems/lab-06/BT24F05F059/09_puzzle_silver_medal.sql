\c view_lab
SELECT name, price
FROM products
WHERE price = (
  SELECT MAX(price)
  FROM products
  WHERE price < (SELECT MAX(price) FROM products)
);