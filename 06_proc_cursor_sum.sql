-- Task 6: Function with cursor loop -- sum every row in accounts.balance
-- Returns total as DECIMAL(14,2)
-- Test: SELECT sum_balances();

CREATE OR REPLACE FUNCTION sum_balances()
RETURNS DECIMAL(14,2) LANGUAGE plpgsql AS $$
DECLARE
  total DECIMAL(14,2) := 0;
  b     DECIMAL(12,2);
  cur   CURSOR FOR SELECT balance FROM accounts;
BEGIN
  DECLARE done INT DEFAULT 0;
  DECLARE b DECIMAL(12,2);
  DECLARE cur CURSOR FOR SELECT balance FROM accounts;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
  SET total = 0;
  OPEN cur;
  loop_label: LOOP
    FETCH cur INTO b;
    IF done THEN LEAVE loop_label; END IF;
    SET total = total + b;
  END LOOP;
  CLOSE cur;
END//
DELIMITER ;
