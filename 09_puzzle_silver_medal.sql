SELECT name
FROM products
WHERE price = (
    SELECT MAX(price)
    FROM products
    WHERE price < (
        SELECT MAX(price) FROM products
    )
);