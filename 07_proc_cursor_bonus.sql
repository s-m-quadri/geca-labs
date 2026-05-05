-- Task 7: Cursor that UPDATEs rows (bonus on payroll)
-- For each row with bonus_eligible = 1, add 100 to salary (use a cursor or a single UPDATE — your README section says "cursor path": use a cursor loop with UPDATE ... WHERE emp_id = current_id)
-- Run: ./run_source.sh proc_lab 07_proc_cursor_bonus.sql
-- Reset DB with 01_setup.sql if you need fresh numbers.

USE proc_lab;
DELIMITER //
DROP PROCEDURE IF EXISTS apply_bonuses//
CREATE PROCEDURE apply_bonuses()
BEGIN
  -- TODO: cursor over (emp_id) where bonus_eligible = 1, loop UPDATE payroll SET salary = salary + 100 WHERE emp_id = ...
  DECLARE done INT DEFAULT 0;
  DECLARE emp_id INT;
  DECLARE cur CURSOR FOR SELECT emp_id FROM payroll WHERE bonus_eligible = 1;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
  OPEN cur;
  loop_fetch: LOOP
    FETCH cur INTO emp_id;
    IF done THEN
      LEAVE loop_fetch;
    END IF;
    UPDATE payroll SET salary = salary + 100 WHERE emp_id = emp_id;
  SET @lab5_bonus_cursor_done := 0;
END//
DELIMITER ;
