-- Puzzle A (riddle)
-- "Two different treasures share the silver tier: not the cheapest, not the priciest.
--  Print their product names." (second-highest **distinct** price)

USE view_lab;

-- TODO: one SELECT; avoid hard-coded price values from the seed in the outer query
SELECT name FROM view_lab.products
WHERE price = (
    SELECT DISTINCT price FROM view_lab.products
    ORDER BY price DESC
    LIMIT 1 OFFSET 1
);