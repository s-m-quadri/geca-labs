
USE proc_lab;
DELIMITER //
DROP PROCEDURE IF EXISTS safe_transfer//
CREATE PROCEDURE safe_transfer(IN from_id INT, IN to_id INT, IN amount DECIMAL(12,2))
BEGIN
  -- TODO: DECLARE donor_balance ... SELECT balance INTO ... IF ...
  -- TODO: UPDATE accounts twice or use transactions mindset (single-threaded lab OK)
  SET @lab5_transfer_todo := 0;
  DECLARE donor_balance DECIMAL(12,2);

  -- Get donor balance
  SELECT balance INTO donor_balance
  FROM accounts
  WHERE id = from_id;

  -- Check if sufficient balance
  IF donor_balance >= amount THEN
    -- Deduct from donor
    UPDATE accounts
    SET balance = balance - amount
    WHERE id = from_id;

    -- Add to receiver
    UPDATE accounts
    SET balance = balance + amount
    WHERE id = to_id;
  END IF;

END//
DELIMITER ;