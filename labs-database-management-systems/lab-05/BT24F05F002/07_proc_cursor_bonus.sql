\c proc_lab

CREATE OR REPLACE PROCEDURE apply_bonuses()
LANGUAGE plpgsql AS $$
DECLARE
  eid INT;
  cur CURSOR FOR 
    SELECT emp_id FROM payroll WHERE bonus_eligible = TRUE;
BEGIN
  OPEN cur;
  LOOP
    FETCH cur INTO eid;
    EXIT WHEN NOT FOUND;
    
    UPDATE payroll
    SET salary = salary + 100
    WHERE emp_id = eid;
    
  END LOOP;
  CLOSE cur;
END;
$$;