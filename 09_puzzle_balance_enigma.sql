-- Puzzle B (riddle)
-- "The smallest balance whispers with the largest: their product is the code."
-- Using only SQL (user variables allowed), set @code := (min balance) * (max balance) from accounts
-- and SELECT @code AS secret_code.

-- TODO: SELECT
--   (SELECT MIN(balance) FROM accounts) *
--   (SELECT MAX(balance) FROM accounts) AS secret_code;
select
  (select min(balance) from accounts) *
  (select max(balance) from accounts) as secret_code;   

                
