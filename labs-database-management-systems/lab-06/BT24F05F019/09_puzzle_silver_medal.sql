-- Puzzle A (riddle)
-- "Two different treasures share the silver tier: not the cheapest, not the priciest.
--  Print their product names." (second-highest distinct price)
\c view_lab

-- TODO: one SELECT; avoid hard-coded price values from the seed in the outer query
select name from products
where price = (
  select distinct price from products
  order by price desc
  limit 1 offset 1
);