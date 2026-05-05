-- Task 7: Procedure that UPDATEs rows (bonus on payroll)
-- For each row with bonus_eligible = TRUE, add 100 to salary using a cursor loop.
-- Reset with 01_setup.sql if you need fresh numbers.
\c proc_lab

CREATE OR REPLACE PROCEDURE apply_bonuses()
LANGUAGE plpgsql AS $$
DECLARE
  eid INT;
  cur CURSOR FOR SELECT emp_id FROM payroll WHERE bonus_eligible = TRUE;
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

-- TODO: CALL apply_bonuses();
-- TODO: SELECT * FROM payroll;
