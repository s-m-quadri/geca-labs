-- Puzzle A (riddle)
-- "Two vaults move coins only if the donor can afford it; otherwise the bank stays silent."
-- Implement safe_transfer(from_id, to_id, amount) on table accounts.
-- Rules: if balance < amount, do not change any row; else subtract from donor, add to receiver.
-- Test: SELECT * FROM accounts; CALL safe_transfer(1,2,100); SELECT * FROM accounts;
USE proc_lab;

DELIMITER $$

CREATE PROCEDURE safe_transfer(
  IN from_id INT,
  IN to_id   INT,
  IN amount  DECIMAL(12,2)
)
BEGIN
  DECLARE from_balance DECIMAL(12,2);

  START TRANSACTION;

  -- Get balance of sender
  SELECT balance INTO from_balance
  FROM accounts
  WHERE id = from_id
  FOR UPDATE;

  -- Check sufficient balance
  IF from_balance < amount THEN
    ROLLBACK;
  ELSE
    -- Deduct from sender
    UPDATE accounts
    SET balance = balance - amount
    WHERE id = from_id;

    -- Add to receiver
    UPDATE accounts
    SET balance = balance + amount
    WHERE id = to_id;

    COMMIT;
  END IF;

END $$

DELIMITER ;
