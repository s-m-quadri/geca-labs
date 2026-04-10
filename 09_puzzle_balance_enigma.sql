-- Puzzle B (riddle)
-- "The smallest balance whispers with the largest: their product is the code."
-- Using only SQL (user variables allowed), set @code := (min balance) * (max balance) from accounts
-- and SELECT @code AS secret_code.

USE proc_lab;

SELECT MIN(balance) * MAX(balance) INTO @code FROM accounts;
SELECT @code AS secret_code;
