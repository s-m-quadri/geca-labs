-- Task 7: Procedure that UPDATEs rows (bonus on payroll)
-- For each row with bonus_eligible = TRUE, add 100 to salary using a cursor loop.
-- Reset with 01_setup.sql if you need fresh numbers.
USE proc_lab;

USE proc_lab;
DELIMITER //
DROP PROCEDURE IF EXISTS apply_bonuses//
CREATE PROCEDURE apply_bonuses()
BEGIN
  OPEN cur;
  LOOP
    FETCH cur INTO eid;
    EXIT WHEN NOT FOUND;
    -- TODO: UPDATE payroll SET salary = salary + 100 WHERE emp_id = eid;
  END LOOP;
  CLOSE cur;
END;
$$;

-- TODO: CALL apply_bonuses();
-- TODO: SELECT * FROM payroll;
CALL apply_bonuses();
SELECT * FROM payroll;
