-- Task 4: Function that returns base increased by pct percent
-- e.g. apply_rate(100, 10) returns 110.00
-- PostgreSQL uses RETURNS, not OUT parameters + DELIMITER
USE proc_lab;

DROP FUNCTION IF EXISTS apply_rate;

DELIMITER //

CREATE FUNCTION apply_rate(
  base DECIMAL(10,2),
  pct DECIMAL(5,2)
)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
  RETURN base + (base * pct / 100);
END //

DELIMITER ;
