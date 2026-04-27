DROP PROCEDURE IF EXISTS apply_bonuses//
CREATE PROCEDURE apply_bonuses()
BEGIN
  -- TODO: cursor over (emp_id) where bonus_eligible = 1, loop UPDATE payroll SET salary = salary + 100 WHERE emp_id = ...
  SET @lab5_bonus_cursor_done := 0;
  DECLARE done INT DEFAULT 0;
  DECLARE eid INT;

  DECLARE cur CURSOR FOR 
    SELECT emp_id FROM payroll WHERE bonus_eligible = 1;

  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

  OPEN cur;

  read_loop: LOOP
    FETCH cur INTO eid;
    IF done THEN
      LEAVE read_loop;
    END IF;

    UPDATE payroll 
    SET salary = salary + 100 
    WHERE emp_id = eid;
  END LOOP;

  CLOSE cur;
END//
DELIMITER ;
DELIMITER ;