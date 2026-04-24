-- Task 4: Stored procedure with OUT parameter (percentage bump)
-- Run: ./run_source.sh proc_lab 04_proc_apply_rate.sql
-- Implement: out_val = base increased by pct percent (e.g. base=100, pct=10 → 110)

USE proc_lab;
DELIMITER //
DROP PROCEDURE IF EXISTS apply_rate//
CREATE PROCEDURE apply_rate(
  IN base DECIMAL(10,2),
  IN pct DECIMAL(5,2),
  OUT out_val DECIMAL(10,2)
)
BEGIN
  SET out_val = base + (base * pct / 100);
END//
DELIMITER ;
