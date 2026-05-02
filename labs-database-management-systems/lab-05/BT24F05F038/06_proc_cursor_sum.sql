-- Task 6: Function with cursor loop -- sum every row in accounts.balance
-- Returns total as DECIMAL(14,2)
-- Test: SELECT sum_balances();
USE proc_lab;

USE proc_lab;
DELIMITER //
DROP PROCEDURE IF EXISTS sum_balances//
CREATE PROCEDURE sum_balances(OUT total DECIMAL(14,2))
BEGIN
  OPEN cur;
  LOOP
    FETCH cur INTO b;
    EXIT WHEN NOT FOUND;
    -- TODO: total := total + b;
  END LOOP;
  CLOSE cur;
  RETURN total;
END;
$$;

-- TODO: SELECT sum_balances();
SELECT sum_balances();
