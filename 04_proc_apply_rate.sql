\c proc_lab;

CREATE OR REPLACE FUNCTION apply_rate(
  base DECIMAL(10,2),
  pct  DECIMAL(5,2)
) 
RETURNS DECIMAL(10,2) 
LANGUAGE plpgsql AS $$
BEGIN
  RETURN base + (base * pct / 100);
END;
$$;