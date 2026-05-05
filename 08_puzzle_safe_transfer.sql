-- Puzzle A (riddle)
-- "Two vaults move coins only if the donor can afford it; otherwise the bank stays silent."
-- Implement safe_transfer(from_id, to_id, amount) on table accounts.
-- Rules: if balance < amount, do not change any row; else subtract from donor, add to receiver.
-- Test: SELECT * FROM accounts; CALL safe_transfer(1,2,100); SELECT * FROM accounts;
\c proc_lab

CREATE OR REPLACE FUNCTION safe_transfer(from_id INT, to_id INT, amount DECIMAL)
RETURNS VOID AS $$
DECLARE
  from_balance DECIMAL;
BEGIN
  SELECT balance INTO from_balance FROM accounts WHERE id = from_id;
  IF from_balance >= amount THEN
    UPDATE accounts SET balance = balance - amount WHERE id = from_id;
    UPDATE accounts SET balance = balance + amount WHERE id = to_id;
  END IF;
END;
$$ LANGUAGE plpgsql;