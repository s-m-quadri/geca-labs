-- Task 7: Cursor that UPDATEs rows (bonus on payroll)
-- For each row with bonus_eligible = 1, add 100 to salary (use a cursor or a single UPDATE — your README section says "cursor path": use a cursor loop with UPDATE ... WHERE emp_id = current_id)
-- Run: ./run_source.sh proc_lab 07_proc_cursor_bonus.sql
-- Reset DB with 01_setup.sql if you need fresh numbers.

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
    UPDATE payroll
    SET salary = salary + 100
    WHERE emp_id = eid;
  END LOOP;
  CLOSE cur;
END;
$$;


-- TODO: CALL apply_bonuses();
-- TODO: SELECT * FROM payroll;
