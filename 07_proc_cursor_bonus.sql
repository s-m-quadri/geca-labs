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
  DECLARE done INT DEFAULT 0;
  DECLARE current_id INT;
  DECLARE cur CURSOR FOR
    SELECT emp_id
    FROM payroll
    WHERE bonus_eligible = 1;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

  OPEN cur;

  bonus_loop: LOOP
    FETCH cur INTO current_id;
    IF done = 1 THEN
      LEAVE bonus_loop;
    END IF;

    UPDATE payroll
    SET salary = salary + 100
    WHERE emp_id = current_id;
  END LOOP;

  CLOSE cur;
END//
DELIMITER ;
