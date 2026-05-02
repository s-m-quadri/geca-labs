-- Task 4: Function that returns base increased by pct percent
-- e.g. apply_rate(100, 10) returns 110.00
-- PostgreSQL uses RETURNS, not OUT parameters + DELIMITER
\c proc_lab

CREATE OR REPLACE FUNCTION apply_rate(base DECIMAL, pct DECIMAL)
RETURNS DECIMAL AS $$
BEGIN
  RETURN base * (1 + pct / 100);
END;
$$ LANGUAGE plpgsql;