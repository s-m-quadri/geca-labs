-- Puzzle A (riddle)
-- "Two different treasures share the silver tier: not the cheapest, not the priciest.
--  Print their product names." (second-highest distinct price)
\c view_lab

-- TODO: one SELECT; avoid hard-coded price values from the seed in the outer query
SELECT prod_name FROM products
WHERE unit_price = (
  SELECT DISTINCT unit_price FROM products
  ORDER BY unit_price DESC
  OFFSET 1 LIMIT 1
);  