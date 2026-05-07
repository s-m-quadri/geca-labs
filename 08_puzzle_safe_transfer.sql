-- Puzzle A (riddle)
-- "Two vaults move coins only if the donor can afford it; otherwise the bank stays silent."
-- Implement safe_transfer(from_id, to_id, amount) on table accounts.
-- Rules: if balance < amount, do not change any row; else subtract from donor, add to receiver.
-- Test: SELECT * FROM accounts; CALL safe_transfer(1,2,100); SELECT * FROM accounts;
\c proc_lab
DROP FUNCTION IF EXISTS safe_transfer(from_id INT, to_id INT, amount NUMERIC);
CREATE FUNCTION safe_transfer(from_id INT, to_id INT, amount NUMERIC)
RETURNS VOID AS $$      