-- Puzzle B (riddle)
-- "The smallest balance whispers with the largest: their product is the code."
-- Compute (MIN balance) * (MAX balance) from accounts and label it secret_code.
-- \c proc_lab

-- TODO: SELECT
--   (SELECT MIN(balance) FROM accounts) *
--   (SELECT MAX(balance) FROM accounts) AS secret_code;

SELECT
  (SELECT MIN(balance) FROM accounts) *
  (SELECT MAX(balance) FROM accounts) AS secret_code;
<<<<<<< HEAD
=======
  
>>>>>>> ae84b5a5 (BT24F05F068)
