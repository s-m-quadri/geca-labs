-- Puzzle A (riddle)
-- "Two vaults move coins only if the donor can afford it; otherwise the bank stays silent."
-- Implement safe_transfer(from_id, to_id, amount) on table accounts.
-- Rules: if balance < amount, do not change any row; else subtract from donor, add to receiver.
-- Run: ./run_source.sh proc_lab 08_puzzle_safe_transfer.sql
-- Test with SELECT * FROM accounts before/after CALL safe_transfer(1,2,100);

CREATE OR REPLACE PROCEDURE safe_transfer(from_id INT, to_id INT, amount DECIMAL)
LANGUAGE plpgsql AS $$
DECLARE
  donor_bal DECIMAL;
BEGIN
  SELECT balance INTO donor_bal FROM accounts WHERE id = from_id;
  IF donor_bal < amount THEN
    RETURN;  -- donor can't afford it; do nothing
  END IF;
  UPDATE accounts SET balance = balance - amount WHERE id = from_id;
  UPDATE accounts SET balance = balance + amount WHERE id = to_id;
END;
$$;
 
-- Test: Alice (id=1) has 1200, Bob (id=2) has 450.50
SELECT * FROM accounts;
CALL safe_transfer(1, 2, 100);   -- should succeed
SELECT * FROM accounts;
CALL safe_transfer(2, 1, 9999);  -- should fail silently
SELECT * FROM accounts;