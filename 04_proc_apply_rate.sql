-- Task 4: Stored procedure with OUT parameter (percentage bump)
-- Run: ./run_source.sh proc_lab 04_proc_apply_rate.sql
-- Implement: out_val = base increased by pct percent (e.g. base=100, pct=10 → 110)

\c proc_lab
CREATE OR REPLACE FUNCTION apply_rate(base DECIMAL, pct DECIMAL)
RETURNS DECIMAL LANGUAGE plpgsql AS $$
BEGIN
  RETURN base * (1 + pct / 100.0);
END;
$$;