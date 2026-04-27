USE proc_lab;
DROP PROCEDURE IF EXISTS safe_transfer;

DELIMITER $$

CREATE PROCEDURE safe_transfer(
  IN from_id INT,
  IN to_id INT,
  IN amount DECIMAL(12,2)
)
BEGIN
  DECLARE donor_balance DECIMAL(12,2);

  SELECT balance INTO donor_balance
  FROM accounts
  WHERE id = from_id;

  IF donor_balance IS NOT NULL AND donor_balance >= amount THEN

    UPDATE accounts
    SET balance = balance - amount
    WHERE id = from_id;

    UPDATE accounts
    SET balance = balance + amount
    WHERE id = to_id;

  END IF;

END$$

DELIMITER ;
