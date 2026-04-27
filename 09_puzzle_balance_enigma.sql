-- Puzzle B (riddle)
-- "The smallest balance whispers with the largest: their product is the code."
-- TODO: two queries or one subquery; no hard-coded numbers from the seed

SELECT MIN(balance) * MAX(balance) AS secret_code
FROM accounts;