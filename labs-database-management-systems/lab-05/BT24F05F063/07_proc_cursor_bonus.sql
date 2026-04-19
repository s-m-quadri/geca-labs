-- Task 7: Cursor that UPDATEs rows (bonus on payroll)
-- For each row with bonus_eligible = 1, add 100 to salary (use a cursor or a single UPDATE — your README section says "cursor path": use a cursor loop with UPDATE ... WHERE emp_id = current_id)
-- Run: ./run_source.sh proc_lab 07_proc_cursor_bonus.sql
-- Reset DB with 01_setup.sql if you need fresh numbers.

USE proc_lab;
DELIMITER //
DROP PROCEDURE IF EXISTS apply_bonuses//
CREATE PROCEDURE apply_bonuses()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE emp_id_val INT;

    DECLARE bonus_cursor CURSOR FOR SELECT emp_id FROM payroll WHERE bonus_eligible = 1;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN bonus_cursor;

    bonus_loop: LOOP
        FETCH bonus_cursor INTO emp_id_val;

        IF done = 1 THEN
            LEAVE bonus_loop;
        END IF;

        UPDATE payroll SET salary = salary + 100 WHERE emp_id = emp_id_val;
    END LOOP;

    CLOSE bonus_cursor;
END//
DELIMITER ;
