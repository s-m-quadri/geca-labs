-- Puzzle B (riddle)
-- "The smallest balance whispers with the largest: their product is the code."
-- Compute (MIN balance) * (MAX balance) from accounts and label it secret_code.
\c proc_lab

USE proc_lab;

SELECT MIN(balance) * MAX(balance) INTO @code
FROM accounts;

SELECT @code AS secret_code;
