-- Task 6: Cursor + loop — sum every row in accounts.balance into OUT total
-- Run: ./run_source.sh proc_lab 06_proc_cursor_sum.sql
-- Test: CALL sum_balances(@t); SELECT @t;

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
    total := total + b;
  END LOOP;
  CLOSE cur;
  RETURN total;
END;
$$;

-- TODO: SELECT sum_balances();
