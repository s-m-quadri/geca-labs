-- Puzzle A (riddle)
-- "Two different treasures share the silver tier: not the cheapest, not the priciest.
--  Print their product names." (second-highest distinct price)

SELECT name
FROM products
WHERE price = (
  SELECT price
  FROM products
  GROUP BY price
  ORDER BY price DESC
  LIMIT 1 OFFSET 1
);
