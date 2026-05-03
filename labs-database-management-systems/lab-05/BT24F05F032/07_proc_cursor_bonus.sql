-- Task 7: Procedure that UPDATEs rows (bonus on payroll)
-- For each row with bonus_eligible = TRUE, add 100 to salary using a cursor loop.
-- Reset with 01_setup.sql if you need fresh numbers.
USE proc_lab;
DROP FUNCTION IF EXISTS apply_bonus;
CREATE FUNCTION apply_bonus() RETURNS VOID LANGUAGE plpgsql AS $$
DECLARE   
  emp RECORD;
  cur CURSOR FOR SELECT emp_id, salary FROM payroll WHERE bonus_eligible = TRUE;
BEGIN         
  OPEN cur;
  LOOP
    FETCH cur INTO emp;
    EXIT WHEN NOT FOUND;
    UPDATE payroll SET salary = salary + 100 WHERE emp_id = emp.emp_id;
  END LOOP;
  CLOSE cur;
END;    
$$;
    
