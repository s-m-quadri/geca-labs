-- Puzzle A (riddle)
-- "Two vaults move coins only if the donor can afford it; otherwise the bank stays silent."
-- Implement safe_transfer(from_id, to_id, amount) on table accounts.
-- Rules: if balance < amount, do not change any row; else subtract from donor, add to receiver.
-- Test: SELECT * FROM accounts; CALL safe_transfer(1,2,100); SELECT * FROM accounts;
USE proc_lab;

DROP PROCEDURE IF EXISTS safe_transfer;

DELIMITER $$

CREATE PROCEDURE safe_transfer(
    IN from_id INT,
    IN to_id   INT,
    IN amount  DECIMAL(12,2)
)
BEGIN
    DECLARE donor_bal DECIMAL(12,2);

    -- Get donor balance
    SELECT balance INTO donor_bal
    FROM accounts
    WHERE id = from_id;

    -- Only proceed if enough balance
    IF donor_bal >= amount THEN

        UPDATE accounts
        SET balance = balance - amount
        WHERE id = from_id;

        UPDATE accounts
        SET balance = balance + amount
        WHERE id = to_id;

    END IF;

END $$

DELIMITER ;