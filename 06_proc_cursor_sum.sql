USE proc_lab;
DROP PROCEDURE IF EXISTS sum_balances;

DELIMITER $$

CREATE PROCEDURE sum_balances(OUT total DECIMAL(14,2))
BEGIN
  DECLARE done INT DEFAULT 0;
  DECLARE b DECIMAL(12,2);

  DECLARE cur CURSOR FOR SELECT balance FROM accounts;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

  SET total = 0;

  OPEN cur;

  read_loop: LOOP
    FETCH cur INTO b;
    IF done THEN
      LEAVE read_loop;
    END IF;

    SET total = total + b;
  END LOOP;

  CLOSE cur;
END$$

DELIMITER ;
