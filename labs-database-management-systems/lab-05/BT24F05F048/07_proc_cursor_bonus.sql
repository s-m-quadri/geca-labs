-- Task 7: Cursor that UPDATEs rows (bonus on payroll)
-- For each row with bonus_eligible = 1, add 100 to salary (use a cursor or a single UPDATE — your README section says "cursor path": use a cursor loop with UPDATE ... WHERE emp_id = current_id)
-- Run: ./run_source.sh proc_lab 07_proc_cursor_bonus.sql
-- Reset DB with 01_setup.sql if you need fresh numbers.

CREATE OR REPLACE PROCEDURE apply_bonuses()
LANGUAGE plpgsql AS $$
DECLARE
  eid INT;
  cur CURSOR FOR SELECT emp_id FROM payroll WHERE bonus_eligible = 1;
BEGIN
  OPEN cur;
  LOOP
    FETCH cur INTO eid;
    EXIT WHEN NOT FOUND;
    UPDATE payroll SET salary = salary + 100 WHERE emp_id = eid;
  END LOOP;
  CLOSE cur;
END;
$$;
 
-- Check before
SELECT * FROM payroll;
CALL apply_bonuses();
-- Check after
SELECT * FROM payroll;