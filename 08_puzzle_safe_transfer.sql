-- Puzzle A (riddle)
-- "Two vaults move coins only if the donor can afford it; otherwise the bank stays silent."
-- Implement safe_transfer(from_id, to_id, amount) on table accounts.
-- Rules: if balance < amount, do not change any row; else subtract from donor, add to receiver.
-- Run: ./run_source.sh proc_lab 08_puzzle_safe_transfer.sql
-- Test with SELECT * FROM accounts before/after CALL safe_transfer(1,2,100);

USE proc_lab;
DELIMITER //
DROP PROCEDURE IF EXISTS safe_transfer//
CREATE PROCEDURE safe_transfer(IN from_id INT, IN to_id INT, IN amount DECIMAL(12,2))
BEGIN
DECLARE donor_balance ... SELECT balance INTO ... IF ...
UPDATE accounts twice or use transactions mindset (single-threaded lab OK)
  SET @lab5_transfer_todo := 0;
END//
DELIMITER ;
