-- Puzzle B (riddle)
-- "The smallest balance whispers with the largest: their product is the code."
USE proc_lab;

-- TODO: two queries or one subquery; no hard-coded numbers from the seed

SELECT @code := MIN(balance) * MAX(balance) AS secret_code
FROM accounts;