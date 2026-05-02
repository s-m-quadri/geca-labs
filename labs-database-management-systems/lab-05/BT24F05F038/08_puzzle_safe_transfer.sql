-- Puzzle A (riddle)
-- "Two vaults move coins only if the donor can afford it; otherwise the bank stays silent."
-- Implement safe_transfer(from_id, to_id, amount) on table accounts.
-- Rules: if balance < amount, do not change any row; else subtract from donor, add to receiver.
-- Test: SELECT * FROM accounts; CALL safe_transfer(1,2,100); SELECT * FROM accounts;
USE proc_lab;

USE proc_lab;
DELIMITER //
DROP PROCEDURE IF EXISTS safe_transfer//
CREATE PROCEDURE safe_transfer(IN from_id INT, IN to_id INT, IN amount DECIMAL(12,2))
BEGIN
  -- TODO: SELECT balance INTO donor_bal FROM accounts WHERE id = from_id;
  -- TODO: IF donor_bal < amount THEN RETURN; END IF;
  -- TODO: UPDATE accounts SET balance = balance - amount WHERE id = from_id;
  -- TODO: UPDATE accounts SET balance = balance + amount WHERE id = to_id;
SELECT balance INTO donor_bal FROM accounts WHERE id = from_id; 
IF donor_bal < amount THEN RETURN; END IF;
UPDATE accounts SET balance = balance - amount WHERE id = from_id;
UPDATE accounts SET balance = balance + amount WHERE id = to_id;

END;
$$;
