-- Task 6: Function with cursor loop -- sum every row in accounts.balance
-- Returns total as DECIMAL(14,2)
-- Test: SELECT sum_balances();
Use proc_lab;
DELIMITER $$

CREATE FUNCTION sum_balances()
RETURNS DECIMAL(14,2)
DETERMINISTIC
BEGIN
  DECLARE total DECIMAL(14,2);

  SELECT SUM(balance) INTO total
  FROM accounts;

  RETURN total;
END $$

DELIMITER ;