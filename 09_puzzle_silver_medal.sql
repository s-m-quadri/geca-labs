-- Puzzle A (riddle)
-- "Two different treasures share the silver tier: not the cheapest, not the priciest.
--  Print their product names." (second-highest distinct price)

<<<<<<< HEAD
-- TODO: one SELECT; avoid hard-coded price values from the seed in the outer query
=======
>>>>>>> d1e2bff (BT24F05F008)
SELECT name
FROM products
WHERE price = (
  SELECT price
  FROM products
  GROUP BY price
  ORDER BY price DESC
  LIMIT 1 OFFSET 1
);