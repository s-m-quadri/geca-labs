-- Puzzle A (riddle)
-- "Two different treasures share the silver tier: not the cheapest, not the priciest.
--  Print their product names." (second-highest distinct price)
\c view_lab

-- TODO: one SELECT; avoid hard-coded price values from the seed in the outer query
-- Connect to the database
\c view_lab

-- Select names where the price matches the second-highest distinct price
SELECT name 
FROM products 
WHERE price = (
    SELECT DISTINCT price 
    FROM products 
    ORDER BY price DESC 
    LIMIT 1 OFFSET 1
);