) RETURNS DECIMAL(10,2) LANGUAGE plpgsql AS $$
BEGIN
  -- TODO: RETURN base + (base * pct / 100);
  RETURN base + (base * pct / 100);
  RETURN NULL;
END;
$$;