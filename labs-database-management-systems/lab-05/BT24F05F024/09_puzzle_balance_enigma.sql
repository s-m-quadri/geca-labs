-- Puzzle B (riddle)
-- "The smallest balance whispers with the largest: their product is the code."
-- Compute (MIN balance) * (MAX balance) from accounts and label it secret_code.

SELECT MIN(balance) * MAX(balance) AS secret_code FROM accounts;
