-- Puzzle A (riddle)
-- "Two vaults move coins only if the donor can afford it; otherwise the bank stays silent."
-- Implement safe_transfer(from_id, to_id, amount) on table accounts.
-- Rules: if balance < amount, do not change any row; else subtract from donor, add to receiver.
-- Test: SELECT * FROM accounts; CALL safe_transfer(1,2,100); SELECT * FROM accounts;

CREATE OR REPLACE PROCEDURE safe_transfer(
  from_id INT,
  to_id   INT,
  amount  DECIMAL(12,2)
) LANGUAGE plpgsql AS $$
DECLARE
  donor_bal DECIMAL(12,2);
BEGIN
  -- TODO: DECLARE donor_balance ... SELECT balance INTO ... IF ...
  DECLARE donor_balance DECIMAL(12,2);
  SELECT balance INTO donor_balance FROM accounts WHERE id = from_id;

  IF donor_balance >= amount THEN
    -- TODO: UPDATE accounts twice or use transactions mindset (single-threaded lab OK)
    UPDATE accounts SET balance = balance - amount WHERE id = from_id;
    UPDATE accounts SET balance = balance + amount WHERE id = to_id;
  END IF;

  SET @lab5_transfer_todo := 0;
END//
DELIMITER ;
