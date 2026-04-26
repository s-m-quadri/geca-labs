-- Task 7: Procedure that UPDATEs rows (bonus on payroll)
-- For each row with bonus_eligible = TRUE, add 100 to salary using a cursor loop.
-- Reset with 01_setup.sql if you need fresh numbers.
USE proc_lab;

DELIMITER $$

CREATE PROCEDURE apply_bonuses()
BEGIN
  DECLARE done INT DEFAULT 0;
  DECLARE eid INT;

  -- Cursor to loop through employees (or accounts table if that's your schema)
  DECLARE cur CURSOR FOR 
    SELECT id FROM employees;

  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

  OPEN cur;

  read_loop: LOOP
    FETCH cur INTO eid;
    IF done THEN
      LEAVE read_loop;
    END IF;

    -- Example update (modify as per your table structure)
    UPDATE employees
    SET salary = salary + 500
    WHERE id = eid;

  END LOOP;

  CLOSE cur;
END $$

DELIMITER ;

-- TODO: CALL apply_bonuses();
-- TODO: SELECT * FROM payroll;
