\c proc_lab
CREATE OR REPLACE FUNCTION apply_rate(base DECIMAL, pct DECIMAL)
RETURNS DECIMAL LANGUAGE plpgsql AS $$
BEGIN
  RETURN base * (1 + pct / 100.0);
END;
$$;