-- Puzzle A (riddle)
-- "Two vaults move coins only if the donor can afford it; otherwise the bank stays silent."
-- Implement safe_transfer(from_id, to_id, amount) on table accounts.
-- Rules: if balance < amount, do not change any row; else subtract from donor, add to receiver.
-- Test: SELECT * FROM accounts; CALL safe_transfer(1,2,100); SELECT * FROM accounts;
\c proc_lab

CREATE OR REPLACE PROCEDURE safe_transfer(
  from_id INT,
  to_id   INT,
  amount  DECIMAL(12,2)
) LANGUAGE plpgsql AS $$
DECLARE
  donor_bal DECIMAL(12,2);
BEGIN
  -- TODO: SELECT balance INTO donor_bal FROM accounts WHERE id = from_id;
  -- TODO: IF donor_bal < amount THEN RETURN; END IF;
  -- TODO: UPDATE accounts SET balance = balance - amount WHERE id = from_id;
  -- TODO: UPDATE accounts SET balance = balance + amount WHERE id = to_id;
  SELECT balance INTO donor_bal 
  FROM accounts 
  WHERE id = from_id;

  -- check if enough balance
  IF donor_bal < amount THEN
    RETURN;
  END IF;

  -- subtract from donor
  UPDATE accounts 
  SET balance = balance - amount 
  WHERE id = from_id;

  -- add to receiver
  UPDATE accounts 
  SET balance = balance + amount 
  WHERE id = to_id;
END;
$$;
SELECT * FROM accounts;
CALL safe_transfer(1, 2, 100);
SELECT * FROM accounts;
