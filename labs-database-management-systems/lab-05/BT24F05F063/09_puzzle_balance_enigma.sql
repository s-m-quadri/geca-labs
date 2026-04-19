-- Puzzle B (riddle)
-- "The smallest balance whispers with the largest: their product is the code."
-- Using only SQL (user variables allowed), set @code := (min balance) * (max balance) from accounts
-- and SELECT @code AS secret_code.

USE proc_lab;

-- two queries or one subquery; no hard-coded numbers from the seed
SET @code := (SELECT MIN(balance) * MAX(balance) FROM accounts);
SELECT @code AS secret_code;
    