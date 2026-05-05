--  Print their product names." (second-highest distinct price)
\c view_lab

-- TODO: one SELECT; avoid hard-coded price values from the seed in the outer query
SELECT name
FROM products
WHERE price = (
  SELECT DISTINCT price
  FROM products
  ORDER BY price DESC
  OFFSET 1 LIMIT 1
);
