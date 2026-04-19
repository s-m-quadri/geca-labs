-- Task 4: Function that returns base increased by pct percent
-- e.g. apply_rate(100, 10) returns 110.00
-- PostgreSQL uses RETURNS, not OUT parameters + DELIMITER
\c proc_lab

CREATE OR REPLACE FUNCTION apply_rate(
  base DECIMAL(10,2),
  pct  DECIMAL(5,2)
) RETURNS DECIMAL(10,2) LANGUAGE plpgsql AS $$
BEGIN
  -- TODO: RETURN base + (base * pct / 100);
  RETURN base + (base * pct / 100);
  RETURN NULL;
END;
$$;
