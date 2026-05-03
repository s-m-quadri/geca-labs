-- Puzzle A (riddle)
-- "Two different treasures share the silver tier: not the cheapest, not the priciest.
--  Print their product names." (second-highest distinct price)
\c view_lab

-- TODO: one SELECT; avoid hard-coded price values from the seed in the outer query
SELECT name
FROM products
WHERE price = (
    SELECT MAX(price)
    FROM products
    WHERE price < (
        SELECT MAX(price) FROM products
    )
);

