-- Puzzle A (riddle)
-- "Two different treasures share the silver tier: not the cheapest, not the priciest.
--  Print their product names." (second-highest distinct price)
\c view_lab

SELECT name
FROM products
WHERE price = (
  SELECT DISTINCT price
  FROM products
  ORDER BY price DESC
  OFFSET 1 LIMIT 1
);
