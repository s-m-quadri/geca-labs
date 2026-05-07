-- Task 4: Function that returns base increased by pct percent
-- e.g. apply_rate(100, 10) returns 110.00
-- PostgreSQL uses RETURNS, not OUT parameters + DELIMITER
\c proc_lab
DROP FUNCTION IF EXISTS apply_rate(base NUMERIC, pct NUMERIC);
CREATE FUNCTION apply_rate(base NUMERIC, pct NUMERIC)
RETURNS NUMERIC AS $$
BEGIN
    RETURN base * (1 + pct / 100);
END;
$$ LANGUAGE plpgsql;
