-- Task 6: Cursor + loop — sum every row in accounts.balance into OUT total
-- Run: ./run_source.sh proc_lab 06_proc_cursor_sum.sql
-- Test: CALL sum_balances(@t); SELECT @t;

USE proc_lab;
DELIMITER $$
DROP PROCEDURE IF EXISTS sum_balances$$
CREATE PROCEDURE sum_balances(OUT total DECIMAL(14,2))
BEGIN
  DECLARE done INT DEFAULT 0;
  DECLARE b DECIMAL(12,2) DEFAULT 0;
  DECLARE cur CURSOR FOR SELECT balance FROM accounts;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

  SET total = 0;

  OPEN cur;
  read_loop: LOOP
    FETCH cur INTO b;
    IF done THEN
      LEAVE read_loop;
    END IF;
    SET total = total + b;
  END LOOP read_loop;
  CLOSE cur;
END$$
DELIMITER ;

CALL sum_balances(@t);
SELECT @t;
